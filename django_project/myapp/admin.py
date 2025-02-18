from django.contrib import admin
from .models import User, Profile, Post, Comment, Tag, PostTag

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag, TagAdmin)
admin.site.register(PostTag)
