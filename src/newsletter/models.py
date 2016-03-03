from django.db import models

# Create your models here.

class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=50, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):    #Python 3.3 is __str__
		return self.email