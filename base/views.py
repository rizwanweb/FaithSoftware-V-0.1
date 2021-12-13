from base.models import Item, LOLO, ShippingLine, Terminal
from base.forms import ClientForm, HeaderForm, HeaderFormset, ItemForm, LoloForm, ShippingForm, TerminalForm
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from refund.models import JobRefund, PidRefund
from jobs.models import Job, PID
from client.models import Client
#from . import utils

from django.views.generic import ListView, FormView

# Create your views here.

#Authentication

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is Incorrect')
    context = {}
    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    recentJobs = Job.objects.all().order_by('-id')[:5]
    recentPids = PID.objects.all().order_by('-id')[:5]
    jobs = Job.objects.all()
    total_jobs = jobs.count()
    pending_bills = Job.objects.filter(billed = False).count()
    pids = PID.objects.all()
    total_pid =  pids.count()
    clients = Client.objects.all()
    jobRefunds = JobRefund.objects.all()
  #  usd = utils.usd

    

    context = {
        'clients': clients,
        'recentJobs': recentJobs,
        'recentPids': recentPids,
  #      'usd': usd,
        'total_pid': total_pid,
        'total_jobs': total_jobs,
        'pending_bills': pending_bills,
        'refunds': jobRefunds,
    }
    return render(request, 'base/home.html', context)


#Products

@login_required(login_url='login')
def baseHome(request):
    items = Item.objects.all()
    terminals = Terminal.objects.all()
    shippings = ShippingLine.objects.all()
    lolos = LOLO.objects.all()

    #Modal Create Item Form
    itemform = ItemForm()
    if request.method == 'POST':
        itemform = ItemForm(request.POST)
        if itemform.is_valid():
            itemform.save()
            return redirect('dashboard')
    
    #Terminal
    terminalform = TerminalForm()
    if request.method == 'POST':
        terminalform = TerminalForm(request.POST)
        if terminalform.is_valid():
            terminalform.save()
            return redirect('dashboard')

    #Shipping Line Form
    shippingform = ShippingForm()
    if request.method == 'POST':
        shippingform = ShippingForm(request.POST)
        if shippingform.is_valid():
            shippingform.save()
            return redirect('dashboard')

    #LoLo Form
    loloform = LoloForm()
    if request.method == 'POST':
        loloform = LoloForm(request.POST)
        if loloform.is_valid():
            loloform.save()
            
            return redirect('dashboard')
    context = {
        'items': items,
        'terminals': terminals,
        'shippings': shippings,
        'lolos': lolos,
        'itemform': itemform,
        'terminal': terminalform,
        'shippingform': shippingform,
        'loloform': loloform,
    }
    return render(request, 'base/basehome.html', context)



class HeaderFormView(LoginRequiredMixin, FormView):
    login_url = 'login'
    template_name = 'base/headers.html'
    form_class = HeaderFormset
    success_url = 'home'
    
def navBar(request):
    clientForm = ClientForm()
    context = {
        'form':clientForm
    }
    return render(request, "navbar.html", context)