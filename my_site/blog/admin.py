from django.contrib import admin
from .models import (
    Author,
    Tag,
    Post,
    Comment)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tag", "date")
    list_display = ("title", "author", "date")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("username", "parent_post")

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comment, CommentAdmin)