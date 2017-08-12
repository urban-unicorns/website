from django import forms
from .models import Project


class ProjectGeo(forms.ModelForm):
    address = forms.CharField(max_length=200)

    class Meta:
        model = Project
        fields = ['type',
                  'description',]