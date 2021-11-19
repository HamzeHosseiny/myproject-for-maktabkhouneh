from django.contrib import admin
from .models import Article, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('parent_id',)

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumbnail_tag', 'Author', 'status', 'published_date', 'Category_to_string']
    list_filter = ['status', 'published_date', 'created_date']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    radio_fields = {"status": admin.VERTICAL}
admin.site.register(Article, ArticleAdmin)
