from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Gripe

def home(request):
    return render(request, 'peoria/home2.html')


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
              'location',
              'description',
    ]


class GripeUpdate(UpdateView):
    model = Gripe
    fields = ['name',
              'location',
              'description',
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

