from client.models import Client
from django.db import models
from jobs.models import PID, Job
# Create your models here.


class Header(models.Model):     # Billing Headers
    title = models.CharField(max_length=200)

    class Meta:
        ordering = [('id')]
    def __str__(self):
        return self.title
    

class Bill(models.Model):
    billNo = models.IntegerField()
    billDate = models.DateField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    salesTaxInvoice = models.IntegerField(unique=True)
    gdNo = models.CharField(max_length=20, blank=True, null=True)
    gdNoDate = models.DateField(blank=True, null=True)
    cashNo = models.CharField(max_length=20, blank=True, null=True)
    cashNoDate = models.DateField(blank=True, null=True)
    grossTotal = models.FloatField(null=True, blank=True)
    charges = models.FloatField(null=True, blank=True)
    rateOfST = models.FloatField(null=True, blank=True)
    salesTax = models.FloatField(null=True, blank=True)
    totalCharges = models.FloatField(null=True, blank=True)
    total = models.FloatField()
    cashRefund = models.FloatField(null=True, blank=True)
    grossBalance = models.FloatField(null=True, blank=True)
    advance = models.FloatField(null=True, blank=True)
    netBalance = models.FloatField(null=True, blank=True)
    note = models.CharField(max_length=500, null=True, blank=True)
    inwords = models.CharField(max_length=500, null=True, blank=True)

    created = models.DateTimeField(null=True, auto_now_add=True)
    updated = models.DateTimeField(null=True, auto_now_add=True)
    class Meta:
        ordering = [('billNo')]
    def __str__(self):
        return str(self.billNo)

    

   
class Particular(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=True, blank=True)
    reciept = models.CharField(max_length=150, null=True, blank=True)
    byUs = models.FloatField(null=True, blank=True)
    byYou = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = [('job')]
    def __str__(self):
        return '{}--Job No-{}'.format(self.title, str(self.job))

class PIDParticular(models.Model):
    pid = models.ForeignKey(PID, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=True, blank=True)
    reciept = models.CharField(max_length=150, null=True, blank=True)
    byUs = models.FloatField(null=True, blank=True)
    byYou = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = [('pid')]
    def __str__(self):
        return '{}--Job No-{}'.format(self.title, str(self.pid))



class PIDBill(models.Model):
    pidbillNo = models.IntegerField()
    billDate = models.DateField()
    pid = models.ForeignKey(PID, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    gdNo = models.CharField(max_length=20, blank=True, null=True)
    gdNoDate = models.DateField(blank=True, null=True)
    cashNo = models.CharField(max_length=20, blank=True, null=True)
    cashNoDate = models.DateField(blank=True, null=True)
    totalCharges = models.FloatField(null=True, blank=True)
    
    cashRefund = models.FloatField(null=True, blank=True)
    grossBalance = models.FloatField(null=True, blank=True)
    advance = models.FloatField(null=True, blank=True)
    netBalance = models.FloatField(null=True, blank=True)
    
    note = models.CharField(max_length=500, null=True, blank=True)
    inwords = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = [('pidbillNo')]
    def __str__(self):
        return str(self.pidbillNo)