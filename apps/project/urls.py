from django.conf.urls import patterns, include, url

urlpatterns = patterns('project.views',
    url(r'^$', 'index', name='project_index'),
)