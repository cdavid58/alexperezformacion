from django.db import models

class Category(models.Model):
	name = models.CharField(max_length = 150)

	def __str__(self):
		return self.name

class Courses(models.Model):
	title = models.CharField(max_length = 150)
	price = models.FloatField()
	miniature = models.URLField(null = True, blank = True)
	category = models.ForeignKey(Category,on_delete = models.CASCADE,null = True, blank = True)

	def __str__(self):
		return self.title
