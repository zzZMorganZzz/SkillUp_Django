from django.contrib import admin
from .models import Tag, Account, Post, Likes

# Register your models here.
admin.site.register(Tag)
admin.site.register(Account)
admin.site.register(Post)
admin.site.register(Likes)