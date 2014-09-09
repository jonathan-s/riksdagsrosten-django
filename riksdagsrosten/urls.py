# encodnig: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin

from riksdagen.views import party, partywithname, singlemp, allmp
from riksdagen.views import polls, home, poll_detail

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('userprofile.urls')),
    url(r'^$', home, name='home'),
    url(r'^parti/$', party, name='party'),
    url(r'^parti/(?P<partyname>\w+)/$', partywithname, name='partywithname'),
    url(r'^ledamot/(?P<mp_id>\d+)/(?P<nameslug>[-\w]+)/$', singlemp, name='singlemp'),
    url(r'^ledamot/(?P<mp_id>\d+)/$', singlemp, name='mpredirect'),
    url(r'^ledamot/$', allmp, name='allmp'),
    url(r'^votering/(?P<doc_id>[A-Öa-ö0-9]+)/$', poll_detail, name='poll_detail'),
    url(r'^votering/tidigare/kategori/(?P<category>\w+)/$', polls, name='pollscat'),
    url(r'^votering/tidigare/kategori/$', polls, name='polls'),
    url(r'^accounts/', include('allauth.urls')),

    # Examples:
    # url(r'^$', 'riksdagsrosten.views.home', name='home'),
    # url(r'^riksdagsrosten/', include('riksdagsrosten.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

