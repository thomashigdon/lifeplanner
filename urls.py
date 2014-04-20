from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^plantree/$', 'plantree.views.treeview'),
    (r'^plantree/(?P<node_id>\d+)/$', 'plantree.views.treeview'),
    (r'^plantree/(?P<node_id>\d+)/change/$', 'plantree.views.change'),
    (r'^plantree/(?P<node_id>\d+)/delete/$', 'plantree.views.delete'),
    (r'^plantree/(?P<node_id>\d+)/add/$', 'plantree.views.add'),
    (r'^plantree/(?P<node_id>\d+)/filter/$', 'plantree.views.filter'),
    (r'^plantree/(?P<node_id>\d+)/finish/$', 'plantree.views.finish'),
    (r'^plantree/(?P<node_id>\d+)/unfinish/$', 'plantree.views.unfinish'),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
