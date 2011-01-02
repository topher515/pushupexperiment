from django.conf.urls.defaults import patterns


urlpatterns = patterns('',
	(r'^$','count.views.front'),
	(r'^workouts/(?P<username>[\w\d]+)/$','count.views.user_counts'),
)