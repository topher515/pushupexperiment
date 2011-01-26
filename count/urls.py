from django.conf.urls.defaults import patterns


urlpatterns = patterns('',
	(r'^$','count.views.front'),
	(r'^add','count.views.add'),
	(r'^users','count.views.users'),
	(r'^workouts/(?P<username>[\w\d]+)/$','count.views.user_counts'),
)