from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^add/', 'weather.map.views.add', name='add'),
    url(r'^clear/', 'weather.map.views.clear', name = 'clear'),                       
    url(r'^$', 'weather.map.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
