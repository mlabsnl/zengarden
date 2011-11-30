import os, settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.BASE_DIR, 'static')}),
    )

urlpatterns += patterns('',
    (r'^$','shop.views.index'),
	(r'^rustgever','shop.views.rustgever'),
	(r'^opkikker','shop.views.opkikker'),
	(r'^bestel', 'shop.views.order'),
	(r'^pay/(?P<amount>[0-9]+)', 'shop.views.pay')
)
