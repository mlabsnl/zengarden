from django.contrib.localflavor.nl.forms import NLZipCodeField
from django.forms.models import ModelForm
from shop.models import Order

class OrderForm(ModelForm):
    customer_zipcode = NLZipCodeField()
    class Meta:
        model = Order
        exclude = ('updated_at','created_at','is_payed','is_shipped')


  