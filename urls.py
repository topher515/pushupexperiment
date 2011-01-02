from django.conf.urls.defaults import *
from django.conf import settings
MEDIA_ROOT = settings.MEDIA_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Example:
	(r'', include('count.urls')),

	(r'^huh/$', 'views.huh'),

	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':MEDIA_ROOT}),

	# Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),
)
