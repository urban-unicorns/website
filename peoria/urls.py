from django.conf.urls import url
from . import views

app_name='peoria'



urlpatterns = [
    #/peoria/
    url(r'^$', views.home, name='home'),
    ]





