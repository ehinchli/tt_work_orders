from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import WorkOrder, Client, Device
from .forms import forms, WorkOrderForm, ClientForm, DeviceForm
from django.http import HttpResponseRedirect


# Create your views here.


def home(request):
    context = {'workOrders': WorkOrder.objects.all()}
    return render(request, 'repair_app/home.html', context)


class WorkOrderList(ListView):
    model = WorkOrder
    template_name = 'repair_app/home.html'
    context_object_name = 'workOrders'
    ordering = ['-date_in']


# -------------------------------------

class WorkOrderDetail(DetailView):
    model = WorkOrder


# views
def step1(request):
    initial = {'fn': request.session.get('fn', None)}
    form = ClientForm(request.POST or None, initial=initial)
    if request.method == 'POST':
        if form.is_valid():
            request.session['fn'] = clean
            return HttpResponseRedirect(reverse('step2'))
    return render(request, 'repair_app/step1.html', {'form': form})


def step2(request):
    form = DeviceForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            request.session['fn'] = form.data()
            return HttpResponseRedirect(reverse('step3'))
    return render(request, 'repair_app/step2.html', {'form': form})


def step3(request):
    form = WorkOrderForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            workorder = form.save(commit=False)
            workorder.client = Client.objects.create(fn=request.session['fn'])
            workorder.device = Device.objects.create(fn=request.session['fn'])
            workorder.save()
            return HttpResponseRedirect(reverse('repair-home'))
    return render(request, 'repair_app/step3.html', {'form': form})



