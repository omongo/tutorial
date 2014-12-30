from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = patterns('',
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>\d+)/$', views.snippet_detail),
)

urlpatterns = format_suffix_patterns(urlpatterns)
