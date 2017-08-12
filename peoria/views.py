from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Gripe, Project

from .forms import ProjectGeo, GripeGeo



from geopy.geocoders import Nominatim



def Chris(request):
    return render(request, 'peoria/chris.html')




def home(request):
    myPavementProjects = Project.objects.filter(type='PV')
    myBikeProjects = Project.objects.filter(type='BK')
    myTrashCanProjects = Project.objects.filter(type='TC')
    myRampsProjects = Project.objects.filter(type='RA')
    mySideWalkProjects = Project.objects.filter(type='SW')



    context = {'myPavementProjects': myPavementProjects,
               'myBikeProjects': myBikeProjects,
               'myTrashCanProjects':myTrashCanProjects,
               'myRampsProjects':myRampsProjects,
               'mySideWalkProjects':mySideWalkProjects,
               }
    return render(request, 'peoria/home2.html', context)

def trash(request):
    return(render(request, 'peoria/trash.html'))


class GripeList(generic.ListView):
    template_name = 'peoria/gripe-list.html'
    context_object_name = 'gripe_list'

    def get_queryset(self):
        return Gripe.objects.all()

class GripeDetail(generic.DetailView):
    model = Gripe
    template_name = 'peoria/gripe-detail.html'


class GripeCreate(CreateView):
    model = Gripe
    fields = ['name',
              'address',
              'description',
    ]


class GripeUpdate(UpdateView):
    model = Gripe
    fields = ['name',
              'address',
              'description',
              'latitude',
              'longitude',
              ]

class GripeDelete(DeleteView):
    model = Gripe
    success_url = reverse_lazy('peoria:gripe-list')

def GripeUpvote(request, pk):
    try:
        selected_gripe = Gripe.objects.get(pk=pk)
    except (KeyError, Gripe.DoesNotExist):
        return HttpResponse("Error, gripe does not exist")
    else:
        mynum = selected_gripe.votes
        selected_gripe.votes = mynum + 1
        selected_gripe.save()

        return HttpResponseRedirect(reverse('peoria:gripe-list'))



class ProjectList(generic.ListView):
    template_name = 'peoria/project-list.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        return Project.objects.all()


class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'peoria/project-detail.html'


class ProjectCreate(CreateView):
    model = Project
    fields = ['latitude',
              'longitude',
              'type',
              'description',
    ]


class ProjectUpdate(UpdateView):
    model = Project
    fields = ['latitude',
              'longitude',
              'type',
              'description',
    ]



class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('peoria:project-list')



def ProjectCreate2(request):
    if request.method == 'POST':
        form = ProjectGeo(request.POST)
        if form.is_valid():
            myAddress = form.cleaned_data['address']
            myType = form.cleaned_data['type']
            myDescription = form.cleaned_data['description']
            geolocator = Nominatim()
            location = geolocator.geocode(myAddress)
            myLatitude = location.latitude
            myLongitude = location.longitude
            a = Project(latitude=myLatitude,
                        longitude=myLongitude,
                        type=myType,
                        description=myDescription,
                        )
            a.save()
        return HttpResponseRedirect(reverse('peoria:project-list'))

    else:
        form = ProjectGeo
        return render(request, 'peoria/project-create.html', {'form':form})



def GripeCreate2(request):
    if request.method == 'POST':
        form = GripeGeo(request.POST)
        if form.is_valid():
            myName = form.cleaned_data['name']
            myAddress = form.cleaned_data['address']
            myDescription = form.cleaned_data['description']
            geolocator = Nominatim()
            location = geolocator.geocode(myAddress)
            myLatitude = location.latitude
            myLongitude = location.longitude
            a = Gripe(name=myName,
                      address=myAddress,
                      description=myDescription,
                      latitude=myLatitude,
                      longitude= myLongitude,
                      )
            a.save()
        return HttpResponseRedirect(reverse('peoria:gripe-list'))

    else:
        form = GripeGeo
        return render(request, 'peoria/gripe-create.html', {'form':form})