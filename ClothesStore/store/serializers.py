from django.contrib.auth import validators
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from .models import Item,CustomeUser,FavList,Rating,SoldItem
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
    class Meta:
        model=Item
        fields='__all__'


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