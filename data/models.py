from django.db import models


# Create your models here.
class Person(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Userid = models.CharField(max_length=20)

    def __str__(self):
        return self.Name