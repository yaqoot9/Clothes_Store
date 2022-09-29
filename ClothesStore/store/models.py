from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class CustomeUser(AbstractUser):
    is_admin=models.BooleanField(default=False)
    is_registered=models.BooleanField(default=False)
    is_worker=models.BooleanField(default=False)


class Item(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    brand=models.CharField(max_length=100)
    gender_choices = [("Female", 'F'), ("Male", 'M')]
    gender = models.CharField(max_length=10, choices=gender_choices)
    category_choices=[("B",'Business'),("S",'Sports'),("C",'Casual'),("F",'Formal')]
    category=models.CharField(max_length=10,choices=category_choices)

class Quantity(models.Model):
    item_id=models.ForeignKey(Item,models.CASCADE,related_name='quntity')
    color_choices=[("Bl",'Black'),("W",'white'),("Y",'Yellow'),("P",'Pink'),("O",'Orange'),("R",'red'),("G",'green'),("B",'blue'),("Gr",'Gray')]
    color=models.CharField(max_length=10,choices=color_choices)
    size_choices=[("S",'Small'),("M",'Medium'),("L",'Large '),("XL",'Extra Large'),("XXL",'Double Extra Larg')]
    size=models.CharField(max_length=10,choices=size_choices)
    quantity_of_item=models.IntegerField()







