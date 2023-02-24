from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'List_Videos/$',List_Videos,name="List_Videos"),
	]