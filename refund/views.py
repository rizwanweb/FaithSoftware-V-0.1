from refund.models import JobRefund
from jobs.models import Job, PID
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import JobRefundForm, PidRefundForm
from jobs.filter import JobRefundFilter

def jobRefund(request, pk):
    job = Job.objects.get(id=pk)
    form = JobRefundForm(initial={'job': job})

    if request.method == 'POST':
        form = JobRefundForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('job_list')
        else:
            print(form.errors)
    context = {
        'form': form,
        'job': job,
    }            
    return render(request, 'refund/job_refund.html', context)


def pidRefund(request, pk):

    pid = PID.objects.get(id=pk)
    form = PidRefundForm(initial={'pid': pid})

    if request.method == 'POST':
        form = PidRefundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pid_list')
    context = {
        'form': form,
        'pid': pid,
    }            
    return render(request, 'refund/pid_refund.html', context)

class JobRefundListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = JobRefund
    template_name = "refund/refund_list.html"
    ordering = ['-job']
    paginate_by = 10
    paginate_orphans = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jobFilter"] = JobRefundFilter(self.request.GET, queryset=self.get_queryset()) 
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return JobRefundFilter(self.request.GET, queryset=queryset).qs


@login_required(login_url='login')
def editRefund(request, pk):
    refund = JobRefund.objects.get(id=pk)
    form = JobRefundForm(instance=refund)
    if request.method == 'POST':
        form = JobRefundForm(request.POST, instance=refund)
        if form.is_valid():
            form.save()
            return redirect('refund_list')
    context = {
        'form': form,
    }
    return render(request, 'refund/job_refund.html', context)