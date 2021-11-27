from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets += (
    ('Extra', {'fields': ('phone_number', 'address',
                            'city', 'state', 'zip_code', 'country', 'credit_card_number', 'credit_card_expiration_date',
                            'credit_card_security_code', 'billing_address', 'billing_city', 'billing_state', 'billing_zip_code',
                            'billing_country', 'shipping_address', 'shipping_city', 'shipping_state', 'shipping_zip_code', 'shipping_country',
                            'credit_card_type',)}),    
)

UserAdmin.fieldsets[2][1]['fields'] += ('is_author', 'special_user')

UserAdmin.list_display += ('is_author', 'is_special_user')

admin.site.register(User, UserAdmin)