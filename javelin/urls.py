from django.conf.urls import patterns, include, url

from apps.jumpbox.views import Jumpbox, PortfolioItem, SendMessage

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', Jumpbox.as_view(first_page = 0), name='about'),
    url(r'^profiles/$', Jumpbox.as_view(first_page = 1), name='profiles'),
	url(r'^portfolio/$', Jumpbox.as_view(first_page = 2), name='portfolio'),
	url(r'^contacts/$', Jumpbox.as_view(first_page = 3), name='contacts'),
    
    url(r'^contacts/send_message/$', SendMessage.as_view(), name='send_message'),
    url(r'^folio/(?P<item_name>[a-z]+)\.html$', PortfolioItem.as_view(), name='portfolio_item'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
