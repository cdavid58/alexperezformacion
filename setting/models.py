from django.db import models

class Advertising_Logo(models.Model):
	img1 = models.ImageField(upload_to = "Advertising")
	img2 = models.ImageField(upload_to = "Advertising")
	img3 = models.ImageField(upload_to = "Advertising")
