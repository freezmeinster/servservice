from django.conf.urls import patterns, include, url

urlpatterns = patterns('issue.views',
    url(r'^$', 'index', name='issue_index'),
)