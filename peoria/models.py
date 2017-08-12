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


