from django.contrib import admin

# Register your models here.

from . import models

from .models import Blog
from .models import Comment

admin.site.register(Blog)
admin.site.register(Comment)


