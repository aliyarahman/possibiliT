from django.conf.urls import patterns, url, include
from app import views


urlpatterns = patterns('',
        url(r'^$', 'django.contrib.auth.views.login'),
        url(r'^login/$', 'django.contrib.auth.views.login'),
        url(r'^logout/$', views.logout_view, name='logout_view'),
        url(r'^index/$', views.index, name='index'),
        url(r'^createprofile/$', views.createprofile, name='createprofile'),
        url(r'^profile/$', views.profile, name='profile'),
)
