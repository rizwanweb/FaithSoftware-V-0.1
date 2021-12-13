from django.db.models import fields
from django.forms import ModelForm
from django import forms

from .models import Bill, PIDBill

class DateInput(forms.DateInput):
    input_type = 'date'


class BillForm(ModelForm):
    class Meta:
        model = Bill
        fields = ['billNo', 'billDate', 'salesTaxInvoice', 'gdNo', 'gdNoDate', 'cashNo', 'cashNoDate', 'grossTotal', 'charges', 'rateOfST', 'salesTax', 'total', 'note']

        

class PIDBillForm(ModelForm):
    class Meta:
        model = PIDBill
        fields = ['pidbillNo', 'billDate', 'gdNo', 'gdNoDate', 'cashNo', 'cashNoDate', 'totalCharges', 'cashRefund', 'grossBalance', 'advance', 'netBalance']

