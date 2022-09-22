from django.db import models

# Create your models here.
class Person(models.Model):
    title = models.CharField(max_length = 120)
    desc = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=100000)
    summary = models.TextField(default='since this is default u will have default')  