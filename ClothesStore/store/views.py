from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Registerserializers, EditSerializers, ChangePasswordSerializers, ItemSerializers,EditItemSerilizers
from .models import CustomeUser, Item


# Create your views here.

class login(APIView):
    def post(self, request):
        context = {}
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login()
            # token, created = Token.objects.get_or_create(user=user)
            # return Response({'token': token.key})

        else:
            context["error"] = "provide valid credentials!"
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class User(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        ser = Registerserializers(data=request.data)
        if ser.is_valid(raise_exception=True):
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            password = request.data['password']
            email = request.data['email']
            username = request.data['username']
            is_admin = request.data['is_admin']
            is_registered = request.data['is_registered']
            is_worker = request.data['is_worker']

            user = CustomeUser.objects.create(
                first_name=first_name,
                last_name=last_name,
                password=password,
                email=email,
                username=username,
                is_admin=is_admin,
                is_registered=is_registered,
                is_worker=is_worker
            )
            user.save()
        return Response(ser.data)

    def put(self, request):
        ser = EditSerializers(instance=request.user, data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
        return Response(ser.data)

    def patch(self, requset):
        object = requset.user
        ser = ChangePasswordSerializers(data=requset.data)
        if ser.is_valid():
            if not object.check_password(ser.data.get("password")):
                return Response({"password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            if ser.data.get("new_password") == ser.data.get("new_password_again"):
                object.set_password(ser.data.get("new_password"))
                object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }
                return Response(response)

        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class ListItem(APIView, PageNumberPagination):

    def get(self, request, name, category, gender, price):
        items = Item.objects.filter(name=name, category=category, gender=gender, price=price)
        results = self.paginate_queryset(items, request, view=self)
        ser = ItemSerializers(results, many=True)
        return self.get_paginated_response(ser.data)


class ItemAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        if request.user.is_worker==True:
            ser=ItemSerializers(data=request.data)
            if ser.is_valid(raise_exception=True):
                name=request.data['name']
                category=request.data['category']
                gender=request.data['gender']
                price=request.data['price']
                brand=request.data['brand']

                items=Item.objects.create(
                    name=name,
                    category=category,
                    gender=gender,
                    price=price,
                    brand=brand
                )
                items.save()
            return Response(ser.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, pk):
        if request.user.is_worker == True:
            p = Item.objects.get(id=pk)
            ser = EditItemSerilizers(instance=p, data=request.data)
            if ser.is_valid(raise_exception=True):
                ser.save()
            return Response(ser.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, pk):
        if request.user.is_worker == True:
            p = Item.objects.filter(id=pk).first()
            p.delete()
            return Response('Deleted!')
        return Response(status=status.HTTP_401_UNAUTHORIZED)
