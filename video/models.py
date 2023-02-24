from django.db import models

class Category(models.Model):
	name = models.CharField(max_length = 150)

	def __str__(self):
		return self.name

class Introduction(models.Model):
	title = models.CharField(max_length = 200)
	url = models.URLField(null = True, blank = True)
	miniature = models.ImageField(upload_to = 'miniature_introduction')
	description = models.TextField()
	video = models.FileField(upload_to = 'video_introduction', null = True, blank = True)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	price = models.FloatField(default = 0)





