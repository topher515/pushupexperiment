from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib import messages

from collections import defaultdict
import datetime

from django.contrib.auth.decorators import login_required

import models
from count import days_ago

def front(request):
	return HttpResponseRedirect(reverse(users))
	
@login_required
def add(request):
	if request.method == 'post':
		workout = models.Workout.get(name=request.POST['workout'])
		
		#models.Count(workout=workout,number=request.POST['number'],
		#	date)
		
		messages.error(request,'Adding not yet implemented')
		
	return HttpResponseRedirect(reverse(user_counts,kwargs={'username':request.user.username}))
	

def users(request):
	users = User.objects.all()
	if users.count() == 1:
		return HttpResponseRedirect(reverse(user_counts,kwargs={'username':users[0].username}))
	
	return render_to_response('users.html',
		{'users':users},
		RequestContext(request))


class countiterator(object):

	def __init__(self,user):
		# Get all the counts in the datebase for this user
		self.counts = models.Count.objects \
			.filter(workout__user=user) \
			.order_by('date')
		self.workouts = set()
		self.group_by_day = defaultdict(dict)
		for c in self.counts:
			self.group_by_day[c.date][c.workout] = c
			self.workouts.add(c.workout)	
		self.workouts = list(self.workouts)

		self._gener = self._counter()
		self.nothing_yet = True

	def __iter__(self):
		return self

	def next(self):
		return self._gener.next()

	def _counter(self):
		first_day = min([x.start_date.date() for x in self.workouts]) # First day
		day = datetime.date.today() - datetime.timedelta(1)
		while day > first_day:


			counts_today = self.group_by_day[day]
				
			toyield = []
			for w in self.workouts:
			
				count = counts_today.get(w)
				if not count:
					toyield.append({'completed':False,
						'date':day,
						'number':0,
						'workout':w,
						'note':''
					})
				elif count.number == 0:
					self.nothing_yet = False
					toyield.append({'completed':False,
						'skipped':True,
						'date':day,
						'number':0,
						'workout':w,
						'note':count.note
					})
				else:
					self.nothing_yet = False
					toyield.append({'completed':True,
						'date':day,
						'number':count.number,
						'workout':w,
						'note':count.note})
				# When printing we want to skip this 'count' if we havent seen any counts yet
				toyield[-1]['skip'] = self.nothing_yet 
			yield toyield

			day -= datetime.timedelta(1)
		raise StopIteration

def user_counts(request,username):
	user = get_object_or_404(User.objects,username=username)
		
	ret = {}
				
	counts = countiterator(user=user)

		
	
	ret['counts'] = counts
	#ret['today_workouts'] = {}
	ret['today'] = datetime.date.today()
	ret['page_user'] = user
	ret['workouts'] = counts.workouts
		
		
	return render_to_response('counts.html',
		ret,
		RequestContext(request))
		
