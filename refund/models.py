from django.db import models
from client.models import Client

from jobs.models import Job, PID

# Create your models here.

class JobRefund(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    rent = models.IntegerField(null=True, blank=True)
    damageCharges = models.IntegerField(null=True, blank=True)
    washingCharges = models.IntegerField(null=True, blank=True)
    refundAmount = models.IntegerField()
    dueDate = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    received = models.BooleanField(default=False)

    def __str__(self):
        return str(self.job.jobNo)


class PidRefund(models.Model):
    pid = models.ForeignKey(PID, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    rent = models.IntegerField(null=True, blank=True)
    damageCharges = models.IntegerField(null=True, blank=True)
    washingCharges = models.IntegerField(null=True, blank=True)
    refundAmount = models.IntegerField()
    dueDate = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    received = models.BooleanField(default=False)

    def __str__(self):
        return str(self.PIDNo)