from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    message = models.TextField(max_length=1000)