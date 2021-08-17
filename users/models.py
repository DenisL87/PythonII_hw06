from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, help_text="User name")
    email = models.CharField(max_length=20, help_text="E-mail")
    password = models.CharField(max_length=20, help_text="Password")
