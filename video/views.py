from setting.models import Advertising_Logo
from django.shortcuts import render
from .models import *

def List_Videos(request):
	al = Advertising_Logo.objects.last()
	img1 = al.img1.url
	img2 = al.img2.url
	img3 = al.img3.url
	videos = Introduction.objects.all()
	category = Category.objects.all()
	
	return render(request,'video/video.html',{'img1':img1,'img2':img2,'img3':img3,
												'list_videos':videos,'category':category
											})
