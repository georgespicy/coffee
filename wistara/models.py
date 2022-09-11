from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class Subcribe(models.Model):
    email = models.EmailField(max_length=50, unique=True)

    def __str__(self):
        return self.email
        
class Menu_Category(models.Model):
    menu_category = models.CharField(max_length=20)

    def __str__(self):
        return self.menu_category
    
    
class Menu(models.Model):
    menu_name = models.CharField(max_length=30)
    menu_discription = models.TextField()
    menu_photo = models.ImageField(validators=[FileExtensionValidator(['jpg', 'jpeg'])], upload_to='menu_photo')
    menu_category = models.ForeignKey(Menu_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.menu_name
    