from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # add additional fields to the user model
    email = models.EmailField(unique=True)
    # add a field for the user's is_author or not
    is_author = models.BooleanField(default=False)
    # add a field for the user's charge start date
    special_user = models.DateTimeField(default=timezone.now)

    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False
    is_special_user.boolean = True

