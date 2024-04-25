from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    user_name = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    def __str__(self):
        return self.user_name