from django.contrib.localflavor.nl.forms import NLZipCodeField
from django.db import models

from django.db import models
from django import forms
from datetime import datetime

class EmailEntry(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(default=datetime.now())

    class Form(forms.Form):
        email = forms.EmailField()

class Order(models.Model):
    PRODUCT_TYPE = (
        ('RU', 'Rustgever'),
        ('OP', 'Opkikkers'),
    )

    product_type = models.CharField(max_length=2, choices=PRODUCT_TYPE)
    product_price = models.DecimalField(max_digits=10,decimal_places=2)
    product_amount = models.IntegerField()
    product_shipment_cost = models.DecimalField(max_digits=10,decimal_places=2)
    customer_name = models.CharField(max_length=255)
    customer_street = models.CharField(max_length=255)
    customer_number = models.CharField(max_length=10)
    customer_zipcode = models.CharField(max_length=7)
    customer_city = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_newsletter = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_payed = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)

