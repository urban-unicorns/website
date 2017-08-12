from django.db import models
from datetime import date, datetime
from django.core.urlresolvers import reverse




class Gripe(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('peoria:gripe-detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-votes']



class Project(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    type = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.type + str(self.pk)

    def get_absolute_url(self):
        return reverse('peoria:project-detail', kwargs={'pk':self.pk})





