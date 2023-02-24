from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^$',Index,name="Index"),
		url(r'About/$',About,name="About"),
		url(r'Category/$',Category,name="Category"),
		url(r'Contact/$',Contact,name="Contact"),
	]