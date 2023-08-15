from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass
class Person(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.person.first_name
class Stock_in(models.Model):
    company_name = models.CharField(max_length=50)
    tile_code = models.CharField(max_length=100)
    tile_size = models.CharField(max_length=100)
    tile_picture = models.ImageField(null = True,blank=True, default="",upload_to="stock/images/")
    box_quantity_in = models.IntegerField(null=False)
    box_capacity = models.FloatField(null=False)
    by_person = models.ForeignKey(Person , on_delete=models.CASCADE)
    date_and_time = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f" ID: {self.id} Company Name: {self.company_name} Tile Code: {self.tile_code}"
    
    
    
    
class Stock_out(models.Model):
    company_name = models.CharField(max_length=50)
    tile_code = models.CharField(max_length=100)
    tile_size = models.CharField(max_length=100)
    tile_picture = models.ImageField(null=True,blank=True, default="",upload_to="stock/images/")
    box_quantity_out = models.IntegerField(null=False)
    box_capacity = models.FloatField(null=False)
    by_person = models.ForeignKey(Person , on_delete=models.CASCADE)
    date_and_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f" ID: {self.id} Company Name: {self.company_name} Tile Code: {self.tile_code}"
    
    
    
    
    
class Stock(models.Model):
    company_name = models.CharField(max_length=50)
    tile_code = models.CharField(max_length=100)
    tile_size = models.CharField(max_length=100)
    tile_picture = models.ImageField(null = True,blank=True, default="")
    box_quantity = models.IntegerField(null=False)
    box_capacity = models.FloatField(null=False)
    

    def __str__(self):
        return f" ID: {self.id} Company Name: {self.company_name} Tile Code: {self.tile_code} Quantity:{self.box_quantity}"
    