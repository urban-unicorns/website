from django.conf.urls import url
from . import views




app_name='peoria'



urlpatterns = [
    #/peoria/
    url(r'^$', views.home, name='home'),
    url(r'^trash/$', views.trash, name='trash'),

    # /nfw/gripe/
    url(r'^gripe/$', views.GripeList.as_view(), name='gripe-list'),
    url(r'^gripe/create/$', views.GripeCreate2, name='gripe-create'),
    url(r'^gripe/(?P<pk>[0-9]+)/$', views.GripeDetail.as_view(), name='gripe-detail'),
    url(r'^gripe/(?P<pk>[0-9]+)/update/$', views.GripeUpdate.as_view(), name='gripe-update'),
    url(r'^gripe/(?P<pk>[0-9]+)/delete/$', views.GripeDelete.as_view(), name='gripe-delete'),
    url(r'^gripe/(?P<pk>[0-9]+)/upvote/$', views.GripeUpvote, name='gripe-upvote'),

    # /nfw/project/
    url(r'^project/$', views.ProjectList.as_view(), name='project-list'),
#    url(r'^project/create/$', views.ProjectCreate.as_view(), name='project-create'),
    url(r'^project/create/$', views.ProjectCreate2, name='project-create'),

    url(r'^project/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view(), name='project-detail'),
    url(r'^project/(?P<pk>[0-9]+)/update/$', views.ProjectUpdate.as_view(), name='project-update'),
    url(r'^project/(?P<pk>[0-9]+)/delete/$', views.ProjectDelete.as_view(), name='project-delete'),

    url(r'^chris/$', views.Chris, name='chris'),
]





