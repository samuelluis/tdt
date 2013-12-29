from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
#     url(r'^$', 'tbt.views.home', name='home'),
#    url(r'^tbt/', include('tbt.foo.s')),
     (r'^traffic_report/get_json', 'traffic_report.views.get_json'),
     (r'^traffic_report/json', 'traffic_report.views.json'),
     (r'^traffic_report/$', 'traffic_report.views.index'),
     (r'^traffic_report/(?P<cars_passed_id>\d+)/$', 'traffic_report.views.detail'),
    (r'^traffic_report/(?P<cars_passed_id>\d+)/results/$', 'traffic_report.views.results'),
    (r'^traffic_report/(?P<cars_passed_id>\d+)/vote/$', 'traffic_report.views.vote'),
    (r'^viewer/view', 'traffic_report.views.viewer'),
    # Uncomment the admin/doc line below to enable admin documentation:
#    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
)
