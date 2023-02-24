from django.shortcuts import render
from .models import *

def Blog(request):
	article = Article.objects.all()
	return render(request,'blog/blog.html',{'article':article,'category':Category.objects.all()})

def Blog_Details(request,pk):
	article = Article.objects
	try:
		pre_article = article.get(pk = int(pk) - 1)
	except Article.DoesNotExist:
		pre_article = None
	try:
		next_article = article.get(pk = int(pk) + 1)
	except Article.DoesNotExist:
		next_article = None
	article = article.get(pk = pk)
	comment = Comment.objects.filter(article = article)
	return render(request,'blog/blog_details.html',{'article':article,'total_comment':len(comment),'pre_article':pre_article,'next_article':next_article,'comments':comment})