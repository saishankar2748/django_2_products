from django.db import models

# Create your models here.
class Person(models.Model):
    title = models.TextField()
    desc = models.TextField()
    price = models.TextField() 