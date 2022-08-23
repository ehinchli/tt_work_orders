from django import forms
from .models import WorkOrder, Device, Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'


class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = ['client', 'device', 'submission_notes']
