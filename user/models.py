from django.db import models

class User(models.Model):
	name = models.CharField(max_length = 40)
	email = models.EmailField(unique = True)
	psswd = models.CharField(max_length = 20)

	def __str__(self):
		return self.email

class Suscribe(models.Model):
	email = models.EmailField(unique = True)