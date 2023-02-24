from setting.models import Advertising_Logo
from django.shortcuts import render
from video.models import Category, Introduction

def List_Courses(request):
	list_introduction = Introduction.objects.all()
	category = Category.objects.all()
	al = Advertising_Logo.objects.last()
	img1 = al.img1.url
	img2 = al.img2.url
	img3 = al.img3.url
	return render(request,'courses/courses.html',{'category':category,'list_courses':list_introduction,
													'img1':img1,'img2':img2,'img3':img3
												})

def Course(request,pk):
	course = Introduction.objects.get(pk=pk)
	return render(request,'courses/course.html',{'course':course})