from django.contrib import admin
from .models import Profile, Follow, Post, Comment

admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(Post)
admin.site.register(Comment)