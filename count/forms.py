from django.forms import ModelForm
import models

class CountForm(ModelForm):
	class Meta:
		model = models.Count

