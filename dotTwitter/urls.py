from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from main.views import saved_tweets, search, home, home_submit, remove_keywords, export, filter

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dotTwitter.views.home', name='home'),
    # url(r'^dotTwitter/', include('dotTwitter.foo.urls')),

    url(r'^$', view=home, name='home'),

    url(r'^remove_keywords/(?P<id>\w+)/$',
        remove_keywords,
        name='remove_keywords'),

    url(r'^home_submit/', view=home_submit, name='home'),
    url(r'^saved_tweets/', view=saved_tweets, name='saved_tweets'),
    url(r'^search/', view=search, name='search'),

    url(r'^filter/(?P<keyword>[\w\ ]+)/(?P<start>\d+)/(?P<end>\d+)/$', view=filter, name='filter'),
    url(r'^filter/(?P<keyword>[\w\ ]+)/$', view=filter, name='filter'),
    url(r'^filter/$', view=filter, name='filter'),

    url(r'^export/(?P<keyword>[\w\ ]+)/(?P<start>\d+)/(?P<end>\d+)/$', view=export, name='export'),
    url(r'^export/(?P<keyword>[\w\ ]+)/$', view=export, name='export'),
    url(r'^export/$', view=export, name='export'),


    url(r'^admin/', include(admin.site.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
