from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'Blog/$',Blog,name="Blog"),
		url(r'Blog_Details/(\d+)/$',Blog_Details,name="Blog_Details"),
	]