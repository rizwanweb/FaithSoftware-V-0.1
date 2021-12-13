from django.forms import ModelForm

from .models import JobRefund, PidRefund

class JobRefundForm(ModelForm):
    class Meta:
        model = JobRefund
        fields = ['job', 'rent', 'damageCharges', 'washingCharges', 'refundAmount', 'dueDate']


class PidRefundForm(ModelForm):
    class Meta:
        model = PidRefund
        fields = '__all__'