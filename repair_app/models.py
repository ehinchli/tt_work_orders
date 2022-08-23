from django.db import models
from django.urls import reverse

CHAR_MAX = 200


class Client(models.Model):
    netid = models.CharField(max_length=8)
    first_name = models.CharField(max_length=CHAR_MAX)
    last_name = models.CharField(max_length=CHAR_MAX)
    affiliation = models.CharField(max_length=CHAR_MAX)
    phone = models.CharField(max_length=CHAR_MAX)
    email = models.CharField(max_length=CHAR_MAX)
    street = models.CharField(max_length=CHAR_MAX)
    city = models.CharField(max_length=CHAR_MAX)
    state = models.CharField(max_length=CHAR_MAX)
    zip = models.IntegerField()
    country = models.CharField(max_length=CHAR_MAX)

    def __str__(self):
        return self.netid


class Device(models.Model):
    serial_number = models.CharField(max_length=CHAR_MAX)
    warranty_type = models.CharField(max_length=CHAR_MAX)
    warranty_expiry = models.DateTimeField()
    misc_hardware = models.CharField(max_length=CHAR_MAX)
    data_backup = models.CharField(max_length=CHAR_MAX)
    find_my_mac = models.CharField(max_length=CHAR_MAX)

    def __str__(self):
        return self.serial_number


class WorkOrder(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    date_in = models.DateTimeField(auto_now=True)
    date_out = models.DateTimeField(null=True, blank=True)
    submission_notes = models.CharField(max_length=2000)
    tech_notes = models.CharField(max_length=2000, blank=True)
    assigned_tech = models.CharField(max_length=CHAR_MAX, blank=True)
    status = models.CharField(max_length=CHAR_MAX, blank=True)
    repair_cost = models.FloatField(null=True)

    def get_absolute_url(self):
        return reverse('post-workOrder-detail', kwargs={'pk': self.pk})
