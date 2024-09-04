from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    pass

class Invoice(models.Model):
    series = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    date = models.DateField()
    seller_name = models.CharField(max_length=100)
    seller_address = models.CharField(max_length=255)
    seller_code = models.CharField(max_length=50)
    seller_vat = models.CharField(max_length=50)
    buyer_name = models.CharField(max_length=100)
    buyer_address = models.CharField(max_length=255)
    buyer_code = models.CharField(max_length=50)
    buyer_vat = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issuer = models.CharField(max_length=100, null=False)  # Make non-nullable

    def __str__(self):
        return f"{self.series} {self.number}"
    
class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=255)
    unit = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    vat_rate = models.DecimalField(max_digits=4, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_price  # Calculate the total price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description
