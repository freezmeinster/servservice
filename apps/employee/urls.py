from django.conf.urls import patterns, include, url

urlpatterns = patterns('employee.views',
    url(r'^$', 'index', name='employee_index'),
    url(r'^office/$', 'office_index', name='office_index'),
)