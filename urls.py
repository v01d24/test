from django.conf.urls.defaults import patterns, include, url

from pr1.autos.views import *
from pr1.autos2.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',
    ('^$',start),
	(r'^preview/(\d)/(\d)/$', preview),
    (r'^search/$', start),
	#(r'^add/man/$', start),
	#(r'^add/mod/$', start),
    (r'^prototype.js$', prototype),
    (r'^add/itm/$', item_add_form),
    (r'^feeds/models-by-man/(\d+)/$', feed_models),
    (r'^edit/itm/$', item_edit_form),
    (r'^delete/itm/$', delete_item),
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
    (r'^catalog2/$', catalog),
    (r'^catalog2/add/$', catalog_add),
    (r'^catalog2/edit/(\d+)/$', catalog_edit),
    (r'^catalog2/del/(\d+)/$', catalog_delete),
    # Examples:
    # url(r'^$', 'pr1.views.home', name='home'),
    # url(r'^pr1/', include('pr1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
