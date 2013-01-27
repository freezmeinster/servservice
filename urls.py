from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^issue/', include('issue.urls')),
    url(r'^employee/', include('employee.urls')),
    url(r'^project/', include('project.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
