from random import choices
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
    menu_name = models.CharField(verbose_name='menu_name', max_length=30)
    menu_discription = models.TextField()
    menu_photo = models.ImageField(validators=[FileExtensionValidator(['jpg', 'jpeg'])], upload_to='menu_photo')
    menu_category = models.ForeignKey(Menu_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.menu_name

class Review(models.Model):
    customer_photo = models.ImageField(validators=[FileExtensionValidator(['jpg', 'jpeg'])], upload_to='customer_photo')
    customer_name = models.CharField(max_length=50)
    customer_review = models.TextField()

    def __str__(self):
        return self.customer_name
    

class Reservation(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    package = [
        ('VVIP', 'VVIP'),
        ('standard', 'standard'),
        ('premium', 'premium')
    ]
    table_package = models.CharField(choices=package, max_length=10)
    sit = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    ]
    table_sit = models.CharField(choices=sit, max_length=10)

    def __str__(self):
        return self.full_name
    