from django.contrib.auth import validators
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from .models import Item,CustomeUser,FavList,Rating,SoldItem,CreditCard,Quantity
from rest_framework import serializers
from django.contrib.auth import password_validation
from .validators import NumberValidator,UppercaseValidator,LowercaseValidator


class Registerserializers(serializers.ModelSerializer):

    class Meta:
        model=CustomeUser
        fields=['is_worker','is_registered','is_admin','username','email','last_name','first_name','password']

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value


class EditSerializers(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    class Meta:
        model=CustomeUser
        fields='__all__'


class ChangePasswordSerializers(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=True)
    new_password =serializers.CharField(required=True)
    new_password_again=serializers.CharField(required=True)

    class Meta:
        model = CustomeUser
        fields='__all__'

class ItemSerializers(serializers.ModelSerializer):
    Quantites=serializers.SerializerMethodField()
    def get_Quantites(self,instance):
        instance.id
        Quantites=Quantity.objects.filter(item_id=instance.id)
        return QuentitySerialzers(Quantites,many=True).data
    class Meta:
        model=Item
        fields=['category','gender','brand','name','price','Quantites']


class ItemCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields ='__all__'


class EditItemSerilizers(serializers.ModelSerializer):
    category=serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    brand = serializers.CharField(required=False)
    price = serializers.CharField(required=False)
    name=serializers.CharField(required=False)
    class Meta:
        model=Item
        fields='__all__'

class FavSerilizers(serializers.ModelSerializer):
    item_id=serializers.CharField(required=False)
    user_id = serializers.CharField(required=False)
    class Meta:
        model=FavList
        fields='__all__'


class SoldItemsSerializers(serializers.ModelSerializer):
    item_id = serializers.CharField(required=False)
    user_id = serializers.CharField(required=False)
    class Meta:
        model=SoldItem
        fields='__all__'

class CreditSerialzers(serializers.ModelSerializer):
    user_id = serializers.CharField(required=False)
    class Meta:
        model=CreditCard
        fields='__all__'

class RatingSerialzers(serializers.ModelSerializer):
    item_id = serializers.CharField(required=False)
    user_id = serializers.CharField(required=False)
    class Meta:
        model=Rating
        fields='__all__'

class QuentitySerialzers(serializers.ModelSerializer):
    item_id = serializers.CharField(required=False)
    class Meta:
        model=Quantity
        fields='__all__'