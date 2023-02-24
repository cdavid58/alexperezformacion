from django.shortcuts import render
from setting.models import Advertising_Logo
from courses.models import Category as cat

def Index(request):
	al = Advertising_Logo.objects.last()
	img1 = al.img1.url
	img2 = al.img2.url
	img3 = al.img3.url
	return render(request,'index.html',{'img1':img1,'img2':img2,'img3':img3})

def Category(request):
	category = cat.objects.all()
	video = Introduction.objects.all()
	return render(request,'category.html',{'category':category,'video':video})

def About(request):
	return render(request,'about.html')

def Contact(request):
	return render(request,'contact.html')