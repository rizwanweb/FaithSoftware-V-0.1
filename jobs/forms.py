from django import forms
from django.forms import ModelForm
from .models import Job, PID


class DateInput(forms.DateInput):
    input_type = 'date'

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
    

    
class PIDForm(ModelForm):
    class Meta:
        model = PID
        fields = '__all__'