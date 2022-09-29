from django.contrib import admin
from .models import Item,Quantity,CustomeUser


# Register your models here.

admin.site.register(Item)
admin.site.register(Quantity)
admin.site.register(CustomeUser)