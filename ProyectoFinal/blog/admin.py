from django.contrib import admin
from .models import Post, Comment, Likes

# Register your models here.

# class PostAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post)
# admin.site.register(PostAdmin)
admin.site.register(Comment)
admin.site.register(Likes)


