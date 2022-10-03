from django.contrib import admin
from .models import Item,Quantity,CustomeUser,Rating,FavList,CreditCard


# Register your models here.

admin.site.register(Item)
admin.site.register(Quantity)
admin.site.register(CustomeUser)
admin.site.register(FavList)
admin.site.register(CreditCard)
admin.site.register(Rating)