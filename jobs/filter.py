from refund.models import JobRefund
from django.db.models import fields
import django_filters

from .models import *

class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = ['jobNo', 'lc', 'client']

class PIDFilter(django_filters.FilterSet):
    class Meta:
        model = PID
        fields = ['PIDNo', 'lc', 'client']

class JobRefundFilter(django_filters.FilterSet):
    class Meta:
        model = JobRefund
        fields = ['job']