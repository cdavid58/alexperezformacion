from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Article_Images)
admin.site.register(Like)
admin.site.register(Comment)