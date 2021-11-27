from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # add additional fields to the user model
    # add a field for the user's is_author or not
    is_author = models.BooleanField(default=False)
    # add a field for the user's phone number
    phone_number = models.CharField(max_length=20)
    # add a field for the user's address
    address = models.CharField(max_length=100)
    # add a field for the user's city
    city = models.CharField(max_length=50)
    # add a field for the user's state
    state = models.CharField(max_length=50)
    # add a field for the user's zip code
    zip_code = models.CharField(max_length=10)
    # add a field for the user's country
    country = models.CharField(max_length=50)
    # add a field for the user's credit card number
    credit_card_number = models.CharField(max_length=16)
    # add a field for the user's credit card expiration date
    credit_card_expiration_date = models.CharField(max_length=7)
    # add a field for the user's credit card security code
    credit_card_security_code = models.CharField(max_length=3)
    # add a field for the user's billing address
    billing_address = models.CharField(max_length=100)
    # add a field for the user's billing city
    billing_city = models.CharField(max_length=50)
    # add a field for the user's billing state
    billing_state = models.CharField(max_length=50)
    # add a field for the user's billing zip code
    billing_zip_code = models.CharField(max_length=10)
    # add a field for the user's billing country
    billing_country = models.CharField(max_length=50)
    # add a field for the user's shipping address
    shipping_address = models.CharField(max_length=100)
    # add a field for the user's shipping city
    shipping_city = models.CharField(max_length=50)
    # add a field for the user's shipping state
    shipping_state = models.CharField(max_length=50)
    # add a field for the user's shipping zip code
    shipping_zip_code = models.CharField(max_length=10)
    # add a field for the user's shipping country
    shipping_country = models.CharField(max_length=50)
    # add a field for the user's credit card type
    credit_card_type = models.CharField(max_length=50)
    # add a field for the user's charge start date
    special_user = models.DateTimeField(default=timezone.now)

    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False
    is_special_user.boolean = True

