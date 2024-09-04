from django.urls import path
from .views import create_invoice, invoice_list, generate_pdf, register, user_login, user_logout, home, loggedin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('loggedin/', loggedin, name='loggedin'),
    path('create_invoice/', create_invoice, name='create_invoice'),
    path('invoice_list/', invoice_list, name='invoice_list'),
    path('generate_pdf/<int:invoice_id>/', generate_pdf, name='generate_pdf'),
]