from django.db import models
from user.models import User

class Category(models.Model):
	name = models.CharField(max_length = 150,unique = True)

	def __str__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length = 250)
	message = models.TextField()
	date = models.CharField(max_length = 12)
	category = models.ForeignKey(Category, on_delete = models.CASCADE )
	url = "article_images_title"
	img_title = models.ImageField(upload_to = url,null = True, blank = True)

	def __str__(self):
		return self.title

class Article_Images(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	url = "article_images"
	img = models.ImageField(upload_to = url)

	def __str__(self):
		return self.article.title

class Like(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	article = models.ForeignKey(Article, on_delete = models.CASCADE)

	def __str__(self):
		return self.article.title


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	date = models.CharField(max_length = 12)
	message = models.TextField(null = True, blank = True)



