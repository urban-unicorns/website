from django import forms
from .models import Project, Gripe


class ProjectGeo(forms.ModelForm):
    address = forms.CharField(max_length=200)

    class Meta:
        model = Project
        fields = ['type',
                  'description',]


class GripeGeo(forms.ModelForm):

    class Meta:
        model = Gripe
        fields = ['name',
                  'address',
                  'description',]


