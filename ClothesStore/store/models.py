import django
from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class TimeStampMixin(models.Model):
    created_at =models. DateField(default=django.utils.timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True







class CustomeUser(AbstractUser,TimeStampMixin):
    is_admin=models.BooleanField(default=False)
    is_registered=models.BooleanField(default=False)
    is_worker=models.BooleanField(default=False)


class Item(TimeStampMixin):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    brand=models.CharField(max_length=100)
    gender_choices = [("Female", 'F'), ("Male", 'M')]
    gender = models.CharField(max_length=20, choices=gender_choices)
    category_choices=[("T-shirt",'T'),("Hoodie",'H'),("Outwear",'O'),("Skirt",'S'),("Pants",'P'),("Dress",'D'),("Long Sleeve",'L'),('Shorts',"SH")]
    category=models.CharField(max_length=20,choices=category_choices)

class Quantity(TimeStampMixin):
    item_id=models.ForeignKey(Item,models.CASCADE,related_name='quntity')
    color_choices=[("Bl",'Black'),("W",'white'),("Y",'Yellow'),("P",'Pink'),("O",'Orange'),("R",'red'),("G",'green'),("B",'blue'),("Gr",'Gray')]
    color=models.CharField(max_length=10,choices=color_choices)
    size_choices=[("S",'Small'),("M",'Medium'),("L",'Large '),("XL",'Extra Large'),("XXL",'Double Extra Larg')]
    size=models.CharField(max_length=10,choices=size_choices)
    quantity_of_item=models.IntegerField()

class SoldItem(TimeStampMixin):
    price=models.IntegerField()
    user_id=models.ForeignKey(CustomeUser,models.CASCADE,related_name='sale')
    item_id=models.ForeignKey(Item,models.CASCADE,related_name='sale')


class Rating(TimeStampMixin):
    rate=models.IntegerField()
    user_id=models.ForeignKey(CustomeUser,models.CASCADE,related_name='rating')
    item_id=models.ForeignKey(Item,models.CASCADE,related_name='rating')


class FavList(models.Model):
    item_id=models.ForeignKey(Item,models.CASCADE,related_name='FavList')
    user_id=models.ForeignKey(CustomeUser,models.CASCADE,related_name='FavList')

class CreditCard(TimeStampMixin):
    user_id=models.ForeignKey(CustomeUser,models.CASCADE,related_name='CreditCard')
    card_type=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    card_number=models.IntegerField()



