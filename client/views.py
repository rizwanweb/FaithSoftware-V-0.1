from django.contrib.auth.decorators import login_required
from jobs.models import Job
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Client
from .forms import ClientForm
from .filter import ClientFilter
# Create your views here.

#@login_required(login_url='login')
class ClientListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Client
    template_name = "client/clients.html'"
    ordering = ['name']
    paginate_by = 10
    paginate_orphans = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clientFilter"] = ClientFilter(self.request.GET, queryset=self.get_queryset()) 
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return ClientFilter(self.request.GET, queryset=queryset).qs


# @login_required(login_url='login')
# def clientsList(request):
#     clients = Client.objects.all().order_by('name')
#     context = {
#         'clients': clients,
#     }
#     return render(request, 'client/clients.html', context)


@login_required(login_url='login')
def clientHome(request, pk):
    client = Client.objects.get(id=pk)
    #jobs = Job.objects.all()
    jobs = client.job_set.all()
    total_jobs = jobs.count()

    print(jobs.count())
    context = {
        'client': client,
        'jobs': jobs,
        'total': total_jobs
    }
    return render(request, 'client/client_home.html', context)



@login_required(login_url='login')
def createClient(request):
    form = ClientForm()

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientslist')
    context = {
        'form': form,
    }
    return render(request, 'client/create_client.html', context)

@login_required(login_url='login')
def editClient(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clientslist')
    context = {
        'form': form,
    }
    return render(request, 'client/create_client.html', context)


