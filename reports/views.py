from refund.models import JobRefund
from .utils import render_to_pdf
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.aggregates import Sum
from num2words import num2words
#Model Imports
from base.models import Company
from jobs.models import PID, Job
from client.models import Client
from billing.models import Bill, Particular, PIDBill, PIDParticular
from datetime import date, date


# Create your views here.

class CalculationSheetPDF(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, pk, *args, **kwargs):
        co = Company.objects.get(pk=1)
        job = Job.objects.get(id=pk)
        context = {
            'co': co,
            'job': job
        }
        pdf = render_to_pdf('reports/calculationsheet.html', context)
        
        return pdf

class PIDCalculationSheetPDF(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, pk, *args, **kwargs):
        co = Company.objects.get(pk=1)
        job = PID.objects.get(id=pk)
        context = {
            'co': co,
            'job': job
        }
        pdf = render_to_pdf('reports/pid_calculationsheet.html', context)
        
        return pdf
    

class JobsReportPDF(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, *args, **kwargs):
        co = Company.objects.get(pk=1)
        startDate = request.GET['start-date']
        endDate = request.GET['end-date']
        jobs = Job.objects.filter(jobDate__range=[startDate, endDate]).order_by('jobNo')
        
        context = {
            'co': co,
            'jobs': jobs,
            'startDate': startDate,
            'endDate': endDate,
        }
        pdf = render_to_pdf('reports/jobreport.html', context)
        return pdf


class STReportPDF(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, *args, **kwargs):
        co = Company.objects.get(pk=1)
        startDate = request.GET['start-date']
        endDate = request.GET['end-date']
        
        # Get List by Date Range
        bills = Bill.objects.filter(billDate__range=[startDate, endDate]).order_by('client')
        # Get sum of columns
        totalCharges = Bill.objects.filter(billDate__range=[startDate, endDate]).values_list('client').annotate(Sum('charges'),Sum('salesTax'), Sum('totalCharges')).order_by('client')
            
        context = {
            'co': co,
            'totalCharges':totalCharges,
            'bills': bills,
            'startDate': startDate,
            'endDate': endDate,
        }
        pdf = render_to_pdf('reports/st_report.html', context)
        return pdf


class CalculationSheetPDF(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, pk, *args, **kwargs):
        co = Company.objects.get(pk=1)
        job = Job.objects.get(id=pk)
        context = {
            'co': co,
            'job': job
        }
        pdf = render_to_pdf('reports/calculationsheet.html', context)
        return pdf

class BillReportPDF(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, pk, *args, **kwargs):
        co = Company.objects.get(pk=1)
        bill = Bill.objects.get(id=pk)
        particulars = Particular.objects.filter(job=bill.job)
        charges = bill.charges
        st = bill.salesTax
        stTotal = charges + st
        totalInWords = num2words(round(bill.total)).upper()
        context = {
            'co': co,
            'inwords': totalInWords,
            'bill': bill,
            'p': particulars,
            'stTotal': stTotal
        }
        pdf = render_to_pdf('reports/bill_report.html', context)
        return pdf


class PIDBillReportPDF(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, pk, *args, **kwargs):
        co = Company.objects.get(pk=1)
        bill = PIDBill.objects.get(id=pk)
        particulars = PIDParticular.objects.filter(pid=bill.pid)
    
        context = {
            'co': co,
            'bill': bill,
            'p': particulars,
        }
        pdf = render_to_pdf('reports/pidbill_report.html', context)
        return pdf


class DamageWaivePDF(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, pk, *args, **kwargs):
        job = Job.objects.get(id=pk)
        context = {
            'job': job
        }
        pdf = render_to_pdf('letters/damage_waive.html', context)
        return pdf

class PIDDamageWaivePDF(LoginRequiredMixin, View):
    login_url = 'login'
    
    def get(self, request, pk, *args, **kwargs):
        pid = PID.objects.get(id=pk)
        today = date.today()
        #
        context = {
            'job': pid,
            'today': today
        }
        pdf = render_to_pdf('letters/damage_waive.html', context)
        print(today)
        return pdf


class JobRefundReportPDF(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, *args, **kwargs):
        name = request.GET['clients']
        client = Client.objects.filter(name=name)

        refunds = client.refund_set.all()
        

        print(refunds)
        context = {

        }
        pdf = render_to_pdf('refund/job_refund_list.html', context)
        return pdf



#DO Preparations

#DO LETTERS
class DOAuthorityLetterPDF(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, pk, *args, **kwargs):
        pid = PID.objects.get(id=pk)
        today = date.today()
        name = pid.shipping.shortname
        #
        context = {
            'job': pid,
            'today': today
        }
        pdf = render_to_pdf('do/authority/'+name.lower()+'.html', context)
        return pdf

#DO UNDERTAKINGS
class DOUndertakingPDF(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, pk, *args, **kwargs):
        pid = PID.objects.get(id=pk)
        today = date.today()
        name = pid.shipping.shortname
        #
        context = {
            'job': pid,
            'today': today
        }
        pdf = render_to_pdf('do/undertaking/'+name.lower()+'.html', context)
        return pdf

