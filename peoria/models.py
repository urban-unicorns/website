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

    PAVEMENT = 'PV'
    BIKE = 'BK'
    TRASHCANS = 'TC'
    RAMPS = 'RA'
    SIDEWALKS = 'SW'
    TYPE_CHOICES = (
        (PAVEMENT, 'Pavement'),
        (BIKE, 'Bike'),
        (TRASHCANS, 'Trashcans'),
        (RAMPS, 'Ramps'),
        (SIDEWALKS, 'Sidewalks'),
    )
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    filename = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.type + str(self.pk)

    def get_absolute_url(self):
        return reverse('peoria:project-detail', kwargs={'pk':self.pk})





