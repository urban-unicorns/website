from django.conf.urls import url
from . import views

app_name='peoria'



urlpatterns = [
    #/peoria/
    url(r'^$', views.home, name='home'),
    url(r'^trash/$', views.trash, name='trash'),

    # /nfw/gripe/
    url(r'^gripe/$', views.GripeList.as_view(), name='gripe-list'),
    url(r'^gripe/create/$', views.GripeCreate.as_view(), name='gripe-create'),
    url(r'^gripe/(?P<pk>[0-9]+)/$', views.GripeDetail.as_view(), name='gripe-detail'),
    url(r'^gripe/(?P<pk>[0-9]+)/update/$', views.GripeUpdate.as_view(), name='gripe-update'),
    url(r'^gripe/(?P<pk>[0-9]+)/delete/$', views.GripeDelete.as_view(), name='gripe-delete'),
    url(r'^gripe/(?P<pk>[0-9]+)/upvote/$', views.GripeUpvote, name='gripe-upvote'),
]





