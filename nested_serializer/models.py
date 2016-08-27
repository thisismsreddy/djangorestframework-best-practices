from django.db import models

# Create your models here.

class Profile(models.Model):
	#In this case we collect all information on single api call we will flech the result
	#And divide them into to models
	phonenumber = models.CharField(max_length=254)
	fave_movie =  models.CharField(max_length=254, blank=True)
	fave_place =  models.CharField(max_length=254, blank=True)

class Person(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	username = models.CharField(max_length=254)
	firstname =  models.CharField(max_length=254, blank=True)
	lastname =  models.CharField(max_length=254, blank=True)

