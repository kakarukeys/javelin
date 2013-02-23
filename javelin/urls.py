from django.conf.urls import patterns, include, url
from apps.jumpbox.views import Jumpbox

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', Jumpbox.as_view(first_page = 0), name='about'),
    url(r'^resume/$', Jumpbox.as_view(first_page = 1), name='resume'),
	url(r'^portfolio/$', Jumpbox.as_view(first_page = 2), name='portfolio'),
	url(r'^contacts/$', Jumpbox.as_view(first_page = 3), name='contacts'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
