from django.db import models

# Create your models here.

class Name(models.Model):
    name_text = models.CharField(max_length = 20)
    def __str__(self):
        return self.name_text

class Owner(models.Model):
    owner_name_text = models.CharField(max_length = 20)
    owner_gender = models.CharField(max_length = 10)
    def __str__(self):
        return self.owner_name_text
