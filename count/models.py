from django.db import models
from django.contrib.auth.models import User

from count import days_ago


class Workout(models.Model):
	name = models.CharField(max_length=64)	
	user = models.ForeignKey(User)
	start_date = models.DateTimeField()
	start_number = models.IntegerField()
	
	def __str__(self): return self.name
	
	def for_today(self):
		return days_ago(self.start_date) + self.start_number
		
	def for_today_sets(self,sets):
		sets_for_today = []
		left_todo = self.for_today()
		each = left_todo / sets
		leftover = left_todo % sets
		for i in xrange(sets):
			sets_for_today.append(each+(1 if leftover > 0 else 0))
			leftover -= 1
		return sets_for_today
		
	def for_today_sets_4(self):
		return self.for_today_sets(4)

class Count(models.Model):
	workout = models.ForeignKey(Workout,unique_for_date="date")
	number = models.IntegerField()
	date = models.DateField()
	note = models.TextField(blank=True)

	def __str__(self): return "%s %s" % (self.number, self.workout.name)