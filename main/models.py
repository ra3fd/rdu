
from django.db import models


class Entry(models.Model):

    callsign = models.CharField(max_length=20)
    band = models.CharField(max_length=10)
    mode = models.CharField(max_length=10)
    country = models.CharField(max_length=30, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.callsign

    class Meta:
        ordering = ('-band', '-datetime')


class Cty(models.Model):

    cty = models.CharField(max_length=26)
    cq = models.CharField(max_length=5, blank=True, null=True)
    itu = models.CharField(max_length=5, blank=True, null=True)
    cont = models.CharField(max_length=5, blank=True, null=True)
    lat = models.CharField(max_length=9, blank=True, null=True)
    lon = models.CharField(max_length=10, blank=True, null=True)
    loctime = models.CharField(max_length=9, blank=True, null=True)
    dxcc = models.CharField(max_length=6, blank=True, null=True)
    pref = models.CharField(max_length=50000, blank=True, null=True)

    def __unicode__(self):
        return self.cty
