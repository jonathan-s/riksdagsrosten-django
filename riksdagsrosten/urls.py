from django.conf.urls import patterns, include, url
from django.contrib import admin

from riksdagen.views import party, partywithname

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^parti/(?P<partyname>\w+)/$', partywithname, name='partywithname'),
    # Examples:
    # url(r'^$', 'riksdagsrosten.views.home', name='home'),
    # url(r'^riksdagsrosten/', include('riksdagsrosten.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
