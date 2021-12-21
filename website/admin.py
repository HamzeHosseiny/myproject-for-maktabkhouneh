from django.contrib import admin
from .models import Contacts, Newsletter

# Register your models here.
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(Contacts, ContactsAdmin)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email',)
    
admin.site.register(Newsletter, NewsletterAdmin)

