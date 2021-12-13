from django.forms.models import modelformset_factory
from billing.models import Header
from django import forms
from django.forms import ModelForm, fields, forms, DateTimeField

from .models import LOLO, Item, ShippingLine, Terminal
from client.models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        

class TerminalForm(ModelForm):
    class Meta:
        model = Terminal
        fields = '__all__'


class ShippingForm(ModelForm):
    class Meta:
        model = ShippingLine
        fields = '__all__'


class LoloForm(ModelForm):
    class Meta:
        model = LOLO
        fields = ['loloname']

class HeaderForm(ModelForm):
    class Meta: 
        model = Header
        fields = '__all__'

HeaderFormset = modelformset_factory(
    Header,
    form=HeaderForm,
    fields='__all__',
    extra=10)