from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    fields_display = ['title', 'created_date', 'status']
admin.site.register(Article, ArticleAdmin)
