from django.shortcuts import render

def Login(request):
	return render(request,'user/login.html')

def Register(request):
	return render(request,'user/register.html')
