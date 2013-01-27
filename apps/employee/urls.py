from django.conf.urls import patterns, include, url

urlpatterns = patterns('employee.views',
    url(r'^$', 'index', name='employee_index'),
)