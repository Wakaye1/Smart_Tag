from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Visitor(models.Model):
    name = models.CharField('Name', max_length=120)
    address = models.CharField(max_length=300)
    Tag_no = models.CharField('Tag Number', max_length=15)
    phone = models.CharField('Contact Phone', max_length=25, blank=True)
    gadget = models.CharField('Gadget', max_length=15)
    Time_in = models.DateTimeField("Timein", blank=True)
    Time_out = models.DateTimeField("TimeOut", blank=True)

    def __str__(self):
        return self.name


