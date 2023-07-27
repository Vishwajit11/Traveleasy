from django.db import models

# Create your models here.
# This is class destination which holds 4 variables the object for this class is in views.py


class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
  

    def __str__(self):
        return self.name


