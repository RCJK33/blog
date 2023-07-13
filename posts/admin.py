from django.contrib import admin

# Register your models here.

from .models import Post,Status

admin.site.register(Post)
admin.site.register(Status)