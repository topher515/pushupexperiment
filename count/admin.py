from django.contrib import admin
import models

class WorkoutAdmin(admin.ModelAdmin):
	pass
	
class CountAdmin(admin.ModelAdmin):
	pass

admin.site.register(models.Workout,WorkoutAdmin)
admin.site.register(models.Count,CountAdmin)