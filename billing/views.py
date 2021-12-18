from billing.forms import BillForm, PIDBillForm
from datetime import datetime
from django.shortcuts import redirect, render
from django.forms.models import inlineformset_factory
from django.views.generic import View, ListView
from .models import Bill, Header, Particular, PIDBill, PIDParticular
from jobs.models import PID, Job
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .filter import BillFilter, PIDBillFilter

# Create your views here.


class BillManagementView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Bill
    template_name = "billing/bill_management.html"
    ordering = ['-billNo']
    paginate_by = 10
    paginate_orphans = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["billFilter"] = BillFilter(self.request.GET, queryset=self.get_queryset()) 
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return BillFilter(self.request.GET, queryset=queryset).qs


@login_required(login_url='login')
def createBill(request, pk):
    today = datetime.today()
    job = Job.objects.get(id=pk)
    titles = Header.objects.values('title')
    headerformset = inlineformset_factory(Job, Particular, fields=('title', 'reciept', 'byYou', 'byUs'), extra=len(titles)+5)
    formset =  headerformset(queryset=Particular.objects.none(), initial=titles)
    
    no = Bill.objects.values_list('salesTaxInvoice').last()
    #no = 6689
    STNo = (no[0] +1)
    billForm = BillForm(initial={'billNo': job.jobNo, 'salesTaxInvoice': STNo, 'billDate': today, 'client':job.client})

    if request.method == 'POST':
        formset = headerformset(request.POST, initial=titles)
        billForm = BillForm(request.POST)
        
        if formset.is_valid() and billForm.is_valid():
            instances = formset.save(commit=False)
            for i in instances:
                i.job = job
                i.save()

            b = billForm.save(commit=False)
            b.job = job
            b.client = job.client
            charges = int(billForm.cleaned_data['charges'])
            st = int(billForm.cleaned_data['salesTax'])
            b.totalCharges = charges + st        
            b.save()
            job.billed = True
            job.save()
            return redirect('pending_bills')
    
    context = {
        'job': job,
        'formset': formset,
        'bf': billForm,
        }
    return render(request, 'billing/create_bill.html', context)

@login_required(login_url='login')
def editBill(request, pk):
    job = Job.objects.get(id=pk)
    billid = Bill.objects.get(job=job)
    headerformset = inlineformset_factory(Job, Particular, fields=('title', 'reciept', 'byYou', 'byUs'),  extra=5)
    formset =  headerformset(instance=job)
    billForm = BillForm(instance=billid)

    if request.method == 'POST':
        formset = headerformset(request.POST, instance=job)
        billForm = BillForm(request.POST, instance=billid)
        if formset.is_valid():
            print("Form is Valid")
            instances = formset.save(commit=False)
            for i in instances:
                i.job = job
                i.save()
            billForm.save()
            return redirect('billHome')
        else:
            print("Form is not valid")
            print(formset.errors)

    context = {
        'job': job,
        'bill': billid,
        'formset': formset,
        'bf': billForm,
        }
    return render(request, 'billing/create_bill.html', context)


class PendingBillsView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Job
    template_name = "billing/pending_bills.html"

class PendingPIDBillsView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = PID
    template_name = "billing/pending_pid_bills.html"
    context_object_name = 'pid_list'


@login_required(login_url='login')
def createPIDBill(request, pk):
    today = datetime.today()
    pid = PID.objects.get(id=pk)
    titles = Header.objects.values('title')
    headerformset = inlineformset_factory(PID, PIDParticular, fields=('title', 'reciept', 'byYou', 'byUs'), extra=len(titles)+5)
    formset =  headerformset(queryset=PIDParticular.objects.none(), initial=titles)
    
    pidbillForm = PIDBillForm(initial={'pidbillNo': pid.PIDNo, 'billDate': today, 'client':pid.client})

    if request.method == 'POST':
        formset = headerformset(request.POST, initial=titles)
        pidbillForm = PIDBillForm(request.POST)
        
        if formset.is_valid() and pidbillForm.is_valid():
            instances = formset.save(commit=False)
            for i in instances:
                i.pid = pid
                i.save()

            p = pidbillForm.save(commit=False)
            p.pid = pid
            p.client = pid.client        
            p.save()
            pid.billed = True
            pid.save()
            return redirect('pending_pid_bills')
        else:
            print(pidbillForm.errors)
    
    
    context = {
        'job': pid,
        'formset': formset,
        'bf': pidbillForm,
        }
    return render(request, 'billing/pid_bill.html', context)


class PIDBillManagementView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = PIDBill
    template_name = "billing/pidbill_management.html"
    ordering = ['-pidbillNo']
    paginate_by = 10
    paginate_orphans = 1
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["billFilter"] =  PIDBillFilter(self.request.GET, queryset=self.get_queryset()) 
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return PIDBillFilter(self.request.GET, queryset=queryset).qs


@login_required(login_url='login')
def editPIDBill(request, pk):
    pid = PID.objects.get(id=pk)
    pidbillid = PIDBill.objects.get(pid=pid)
    headerformset = inlineformset_factory(PID, PIDParticular, fields=('title', 'reciept', 'byYou', 'byUs'),  extra=5)
    formset =  headerformset(instance=pid)
    billForm = PIDBillForm(instance=pidbillid)

    if request.method == 'POST':
        formset = headerformset(request.POST, instance=pid)
        billForm = PIDBillForm(request.POST, instance=pidbillid)
        if formset.is_valid():
            print("Form is Valid")
            instances = formset.save(commit=False)
            for i in instances:
                i.pid = pid
                i.save()
            billForm.save()
            return redirect('pidbillHome')
        else:
            print("Form is not valid")
            print(formset.errors)

    context = {
        'job': pid,
        'bill': pidbillid,
        'formset': formset,
        'bf': billForm,
        }
    return render(request, 'billing/pid_bill.html', context)