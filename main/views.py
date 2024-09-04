from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('loggedin')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')


from django.shortcuts import render, redirect
from .forms import InvoiceForm, InvoiceItemForm
from .models import Invoice, InvoiceItem
from django.forms import modelformset_factory

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(html, dest=result)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return result

@login_required
def create_invoice(request):
    InvoiceItemFormSet = modelformset_factory(InvoiceItem, form=InvoiceItemForm, extra=1)
    
    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST)
        formset = InvoiceItemFormSet(request.POST, queryset=InvoiceItem.objects.none())
        if invoice_form.is_valid() and formset.is_valid():
            invoice = invoice_form.save(commit=False)
            invoice.user = request.user
            invoice.issuer = request.user.username
            invoice.save()
            for form in formset:
                item = form.save(commit=False)
                item.invoice = invoice
                item.save()
            return redirect('invoice_list')
    else:
        invoice_form = InvoiceForm()
        formset = InvoiceItemFormSet(queryset=InvoiceItem.objects.none())
    
    return render(request, 'create_invoice.html', {'invoice_form': invoice_form, 'formset': formset})

@login_required
def invoice_list(request):
    invoices = Invoice.objects.filter(user=request.user)
    return render(request, 'invoice_list.html', {'invoices': invoices})

@login_required
def generate_pdf(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id, user=request.user)
    items = InvoiceItem.objects.filter(invoice=invoice)
    context = {'invoice': invoice, 'items': items}
    pdf = render_to_pdf('invoice_pdf.html', context)
    return pdf

def home(request):
    if request.user.is_authenticated:
        return redirect('loggedin')
    return render(request, 'home.html')

@login_required
def loggedin(request):
    return render(request, 'loggedin.html')