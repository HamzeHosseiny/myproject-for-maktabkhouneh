from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
