from django.contrib import admin
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display=('pk','title','content','created_at','updated_at','image')

admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','content','created_at','article_id')

admin.site.register(Comment,CommentAdmin)
