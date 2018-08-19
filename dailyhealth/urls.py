from django.conf.urls import patterns, url
from dailyhealth import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^capacity/$', views.capacity, name='capacity')
)