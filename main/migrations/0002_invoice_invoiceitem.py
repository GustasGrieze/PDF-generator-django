# Generated by Django 4.2.13 on 2024-05-31 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('seller_name', models.CharField(max_length=100)),
                ('seller_address', models.CharField(max_length=255)),
                ('seller_code', models.CharField(max_length=50)),
                ('seller_vat', models.CharField(max_length=50)),
                ('buyer_name', models.CharField(max_length=100)),
                ('buyer_address', models.CharField(max_length=255)),
                ('buyer_code', models.CharField(max_length=50)),
                ('buyer_vat', models.CharField(max_length=50)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('unit', models.CharField(max_length=50)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vat_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='main.invoice')),
            ],
        ),
    ]
