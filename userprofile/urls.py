from django.conf.urls import patterns, include, url

from userprofile.views import userprofile
from userprofile.views import openprofile
from userprofile.views import user_settings


urlpatterns = patterns('',
    url(r'^profil/$', userprofile, name='userprofile'),
    url(r'^profil/installningar/$', user_settings, name='usersettings'),
    url(r'^anvandare/(?P<username>\w+)/$', openprofile, name='openprofile'),
)