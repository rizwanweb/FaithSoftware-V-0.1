from django.db import models

from client.models import Client
from base.models import Item, LOLO, ShippingLine, Terminal

# Create your models here.

class Job(models.Model):
    DUTYTYPE = (
        ('%', '%'),
        ('F', 'F')
    )
    jobNo = models.IntegerField(unique=True)
    jobDate = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    containers = models.IntegerField(null=True, blank=True)
    size = models.IntegerField(null=True, blank=True)
    packages = models.CharField(max_length=200)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, null=True, blank=True)
    vessel = models.CharField(max_length=200)
    igm = models.IntegerField()
    igmDate = models.DateField()
    index = models.IntegerField()
    lc = models.CharField(max_length=200, null=True, blank=True)
    lcDate = models.DateField(null=True, blank=True)
    bl = models.CharField(max_length=200)
    blDate = models.DateField(null=True, blank=True)
    dv = models.FloatField()
    quantity = models.FloatField()

    exRate = models.FloatField()
    importValueUSD = models.FloatField()
    pkr = models.IntegerField()
    insurance = models.IntegerField(null=True, blank=True)
    landingCharges = models.IntegerField()
    importValue = models.IntegerField()
    dutyType = models.CharField(max_length=5, choices=DUTYTYPE, null=True, blank=True)
    rateOfDuty = models.FloatField(null=True, blank=True)
    customDuty = models.IntegerField(null=True, blank=True)
    rateOfAddDuty = models.FloatField(null=True, blank=True)
    addCustomDuty = models.IntegerField(null=True, blank=True)
    rateOfST = models.FloatField(null=True, blank=True)
    salesTax = models.IntegerField(null=True, blank=True)
    rateOfIT = models.FloatField(null=True, blank=True)
    incomeTax = models.IntegerField(null=True, blank=True)
    rateOfCess = models.FloatField(null=True, blank=True)
    cess = models.IntegerField(null=True, blank=True)
    rateOfRD = models.FloatField(null=True, blank=True)
    rd = models.IntegerField(null=True, blank=True)
    rateOfAD = models.FloatField(null=True, blank=True)
    antiDumping = models.IntegerField(null=True, blank=True)
    excise = models.IntegerField(null=True, blank=True)
    terminalCharges = models.IntegerField(null=True, blank=True)
    do = models.IntegerField(null=True, blank=True)
    deposit = models.IntegerField(null=True, blank=True)
    advanceRent = models.IntegerField(null=True, blank=True)
    loloCharges = models.IntegerField(null=True, blank=True)
    total = models.IntegerField()

    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE)
    shipping = models.ForeignKey(ShippingLine, on_delete=models.CASCADE)
    lolo = models.ForeignKey(LOLO, on_delete=models.CASCADE, null=True, blank=True)
    faithCheck = models.IntegerField(null=True, blank=True)

    billed = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.jobNo)


#PID
class PID(models.Model):
    DUTYTYPE = (
        ('%', '%'),
        ('F', 'F')
    )
    PIDNo = models.IntegerField(unique=True)
    Date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    containers = models.IntegerField(null=True, blank=True)
    size = models.IntegerField(null=True, blank=True)
    packages = models.CharField(max_length=200)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, null=True, blank=True)
    vessel = models.CharField(max_length=200)
    igm = models.IntegerField()
    igmDate = models.DateField()
    index = models.IntegerField()
    lc = models.CharField(max_length=200, null=True, blank=True)
    lcDate = models.DateField(null=True, blank=True)
    bl = models.CharField(max_length=200)
    blDate = models.DateField(null=True, blank=True)
    dv = models.FloatField()
    quantity = models.FloatField()

    exRate = models.FloatField()
    importValueUSD = models.FloatField()
    pkr = models.IntegerField()
    insurance = models.IntegerField(null=True, blank=True)
    landingCharges = models.IntegerField()
    importValue = models.IntegerField()
    dutyType = models.CharField(max_length=5, choices=DUTYTYPE, null=True, blank=True)
    rateOfDuty = models.FloatField(null=True, blank=True)
    customDuty = models.IntegerField(null=True, blank=True)
    rateOfAddDuty = models.FloatField(null=True, blank=True)
    addCustomDuty = models.IntegerField(null=True, blank=True)
    rateOfST = models.FloatField(null=True, blank=True)
    salesTax = models.IntegerField(null=True, blank=True)
    rateOfIT = models.FloatField(null=True, blank=True)
    incomeTax = models.IntegerField(null=True, blank=True)
    rateOfCess = models.FloatField(null=True, blank=True)
    cess = models.IntegerField(null=True, blank=True)
    rateOfRD = models.FloatField(null=True, blank=True)
    rd = models.IntegerField(null=True, blank=True)
    rateOfAD = models.FloatField(null=True, blank=True)
    antiDumping = models.IntegerField(null=True, blank=True)
    excise = models.IntegerField(null=True, blank=True)
    terminalCharges = models.IntegerField(null=True, blank=True)
    advanceRent = models.IntegerField(null=True, blank=True)
    do = models.IntegerField(null=True, blank=True)
    deposit = models.IntegerField(null=True, blank=True)
    loloCharges = models.IntegerField(null=True, blank=True)
    total = models.IntegerField()

    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE)
    shipping = models.ForeignKey(ShippingLine, on_delete=models.CASCADE)
    lolo = models.ForeignKey(LOLO, on_delete=models.CASCADE, null=True, blank=True)
    faithCheck = models.IntegerField(null=True, blank=True)

    billed = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.PIDNo)