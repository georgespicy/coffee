from pyexpat import model
from django.db import models

# Create your models here.

class Subcribe(models.Model):
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.email
        
class Menu(model.Model):
    menu_name = models.CharField(max_length=30)
    menu_discription = models.TextField()
    menu_photo = models.ImageField()