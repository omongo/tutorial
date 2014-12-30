from django.conf.urls import patterns, url

from snippets import views

urlpatterns = patterns('',
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>\d+)/$', views.snippet_detail),
)
