from django.db import models

class Person(models.Model):
	# in this exaple we need a extra filed like phone_number but we dont want save to our database 
	# we are gonna verifi this user with some third pary api
	username = models.CharField(max_length=254)
	firstname =  models.CharField(max_length=254, blank=True)
	lastname =  models.CharField(max_length=254, blank=True)

	def __unicode__(self):
		return self.user.firstname
