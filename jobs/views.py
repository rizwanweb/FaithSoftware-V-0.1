import io
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from reports.utils import render_to_pdf

from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .models import PID, Job
from .forms import JobForm, PIDForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .filter import JobFilter, PIDFilter


# Create your views here.


#@login_required(login_url='login')
class JobCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Job
    form_class = JobForm
    template_name = 'jobs/create_job.html'
    success_url = reverse_lazy('job_list')

    def form_invalid(self, form: JobForm) -> HttpResponse:
        print(form.errors)
        return super().form_invalid(form)
    

@login_required(login_url='login')
def editJob(request, pk):
    job = Job.objects.get(id=pk)
    form = JobForm(instance=job)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    context = {
        'form': form,
    }
    return render(request, 'jobs/create_job.html', context)

#@login_required(login_url='login')
class JobListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Job
    template_name = "jobs/job_list.html"
    #context_object_name = 'jobs'
    ordering = ['-jobNo']
    paginate_by = 10
    paginate_orphans = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jobFilter"] = JobFilter(self.request.GET, queryset=self.get_queryset()) 
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return JobFilter(self.request.GET, queryset=queryset).qs
    
    
def sendMail(request, pk):
    job = Job.objects.get(id=pk)

    if request.method == 'POST':
        emailTo = request.POST['emailTo']
        emailSubject = request.POST['emailSubject']
        #emailFile = request.POST['emailFile'] 
        emailMsg = request.POST ['emailMsg']
        fromEmail = settings.EMAIL_HOST_USER
        print(emailTo)

        send_mail(
            emailSubject,
            emailMsg,
            fromEmail,
            [emailTo,], 
            
            #emailFile,
        )
        #generate_obj_pdf(job.id)
        if send_mail:
            return redirect('job_list')
    context = {
        'job': job,
    }
    return render(request, 'jobs/email.html', context)

#XHTML 2 PDF

#FOR EMAIL
def generate_obj_pdf(instance_id):
     obj = Job.objects.get(id=instance_id)
     context = {'instance': obj}
     pdf = render_to_pdf('jobs/reports/calculationsheet.html', context)
     filename = "mytestpdf.pdf"
     #obj.save(filename, File(io.BytesIO(pdf.content)))


class JobsReportPDF(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, *args, **kwargs):
        startDate = request.GET['start-date']
        endDate = request.GET['end-date']
        jobs = Job.objects.filter(jobDate__range=[startDate, endDate]).order_by('jobNo')
        
        context = {
            'jobs': jobs,
            'startDate': startDate,
            'endDate': endDate,
        }
        pdf = render_to_pdf('jobs/reports/jobreport.html', context)
        return pdf


class PIDCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = PID
    form_class = PIDForm
    template_name = 'jobs/create_pid.html'
    success_url = reverse_lazy('pid_list')

    def form_invalid(self, form: PIDForm) -> HttpResponse:
        print(form.errors)
        return super().form_invalid(form)

@login_required(login_url='login')
def editPID(request, pk):
    pid = PID.objects.get(id=pk)
    form = PIDForm(instance=pid)
    if request.method == 'POST':
        form = PIDForm(request.POST, instance=pid)
        if form.is_valid():
            form.save()
            return redirect('pid_list')
    context = {
        'form': form,
    }
    return render(request, 'jobs/create_pid.html', context)

#@login_required(login_url='login')
class PIDListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = PID
    template_name = "jobs/pid_list.html"
    #context_object_name = 'jobs'
    ordering = ['-PIDNo']
    paginate_by = 10
    paginate_orphans = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pidFilter"] = PIDFilter(self.request.GET, queryset=self.get_queryset()) 
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return JobFilter(self.request.GET, queryset=queryset).qs
