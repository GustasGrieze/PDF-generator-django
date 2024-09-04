from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms
from .models import Invoice, InvoiceItem

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'series', 'number', 'date', 'seller_name', 'seller_address',
            'seller_code', 'seller_vat', 'buyer_name', 'buyer_address',
            'buyer_code', 'buyer_vat', 'total_amount', 'issuer'
        ]
class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['description', 'unit', 'quantity', 'unit_price', 'vat_rate']
