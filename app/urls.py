from django.conf.urls import patterns, url, include
from app import views


urlpatterns = patterns('',
        url(r'^$', 'django.contrib.auth.views.login'),
        url(r'^login/$', 'django.contrib.auth.views.login'),
        url(r'^logout/$', views.logout_view, name='logout_view'),
        url(r'^index/$', views.index, name='index'),
        url(r'^basic_info/$', views.basic_info, name='basic_info'),
        url(r'^identities/$', views.identities, name='identities'),
        url(r'^more_about/$', views.more_about, name='more_about'),
        url(r'^looking_for/$', views.looking_for, name='looking_for'),
        url(r'^contact_info/$', views.contact_info, name='contact_info'),
        url(r'^create_account/$', views.create_account, name='create_account'),
        url(r'^update_profile/$', views.update_profile, name='update_profile'),
        url(r'^settings/$', views.settings, name='settings'),
        url(r'^send_message/$', views.send_message, name='send_message'),
)
