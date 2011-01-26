import datetime

def days_ago(day):
	if type(day) == datetime.datetime: # We'll be nice about take a datetime
		day = day.date()
	return (datetime.date.today() - day).days