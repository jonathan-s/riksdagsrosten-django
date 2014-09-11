# encoding: utf-8

from django.conf.urls import patterns, include, url

from userprofile.views import userprofile
from userprofile.views import openprofile
from userprofile.views import user_settings
from userprofile.views import poll_detail_vote
from userprofile.views import logout


urlpatterns = patterns('',
    url(r'^profil/$', userprofile, name='userprofile'),
    url(r'^profil/logout/$', logout, name='logout'),
    url(r'^profil/installningar/$', user_settings, name='usersettings'),
    url(r'^anvandare/(?P<username>\w+)/$', openprofile, name='openprofile'),
    url(r'^votering/(?P<doc_id>[A-Öa-ö0-9]+)/(?P<doc_item>\d+)/(?P<vote>Ja|Nej)/$',
        poll_detail_vote, name='poll_vote'),


)