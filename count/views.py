from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

import datetime

import models
from count import days_ago

def front(request):
	return HttpResponseRedirect(reverse(user_counts,kwargs={'username':'chris'}))
	

def user_counts(request,username):
	user = get_object_or_404(User.objects,username=username)
	
	counts = models.Count.objects \
		.filter(workout__user=user) \
		.order_by('-date')
	
	ret = {}
		
	group_by_date = []
	last_count_date = None
	workouts = set()
	for c in counts:
		if last_count_date == c.date:
			group_by_date[-1].append(c)
		else:
			group_by_date.append([c])
		workouts.add(c.workout)
		last_count_date = c.date
		
	ret['counts'] = group_by_date
	ret['today_workouts'] = {}
	ret['today'] = datetime.date.today()
	ret['page_user'] = user
	
	for workout in workouts:
		ret['today_workouts'][workout.name] = \
			days_ago(workout.start_date) + workout.start_number + 1
		
	return render_to_response('counts.html',
		ret,
		RequestContext(request))
		
