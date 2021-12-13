from django.db.models import fields
import django_filters

from .models import *

class BillFilter(django_filters.FilterSet):
    class Meta:
        model = Bill
        fields = ['billNo', 'gdNo',]

class PendingBillFilter(django_filters.FilterSet):
    class Meta:
        model = Bill
        fields = ['billNo',]


class PendingPIDBillFilter(django_filters.FilterSet):
    class Meta:
        model = PIDBill
        fields = ['pidbillNo',]

class PIDBillFilter(django_filters.FilterSet):
    class Meta:
        model = PIDBill
        fields = ['pidbillNo', 'gdNo',]