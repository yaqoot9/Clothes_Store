from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import permission_classes, api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Registerserializers, EditSerializers, ChangePasswordSerializers, ItemSerializers, \
    EditItemSerilizers, FavSerilizers, SoldItemsSerializers, CreditSerialzers, RatingSerialzers, QuentitySerialzers,ItemCreateSerializers
from .models import CustomeUser, Item, FavList, CreditCard, SoldItem, Rating, Quantity
from .decorators import registerd_only, registerd_only_pk, worker_only, worker_only_pk,is_auth,is_auth_pk
from django.db.models import Q, Sum, Max, QuerySet,Count,Avg



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





class ItemAPI(APIView, PageNumberPagination):
    def get(self, request, name, category, gender, price):
        query=Q()
        if name is not None:
            query = query & Q(name=name)

        if gender is not None:
             query = query & Q(category=category)

        if gender is not None:
            query = query & Q(gender=gender)

        if price is not None:
            query = query & Q(price=price)
        items = Item.objects.filter(query)
        results = self.paginate_queryset(items, request, view=self)
        ser = ItemSerializers(results, many=True)
        return self.get_paginated_response(ser.data)

    @is_auth
    @worker_only
    def post(self, request):
        ser = ItemCreateSerializers(data=request.data)
        if ser.is_valid(raise_exception=True):
            name = request.data['name']
            category = request.data['category']
            gender = request.data['gender']
            price = request.data['price']
            brand = request.data['brand']
            items = Item.objects.create(
                name=name,
                category=category,
                gender=gender,
                price=price,
                brand=brand
            )

            items.save()

        return Response(ser.data)
    @is_auth_pk
    @worker_only_pk
    def put(self, request, pk):
        p = Item.objects.get(id=pk)
        ser = EditItemSerilizers(instance=p, data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
        return Response(ser.data)

    @is_auth_pk
    @worker_only_pk
    def delete(self, request, pk):
        p = Item.objects.filter(id=pk).first()
        p.delete()
        return Response('Deleted!')


class BuyItem(APIView):
    permission_classes = (IsAuthenticated,)

    @registerd_only_pk
    def post(self, request, pk):

        user = request.user
        try:
            credit = CreditCard.objects.get(user_id=user)
        except:
            return Response("Please enter your credit credentials!")

        item_id = Item.objects.get(id=pk)
        price = item_id.price
        solditem = SoldItem.objects.create(
            user_id=user,
            item_id=item_id,
            price=price
        )
        ser = FavSerilizers(instance=solditem, data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()

        return Response(ser.data)


class FavListAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @registerd_only_pk
    def post(self, request, pk):
        user = request.user
        item_id = Item.objects.get(id=pk)
        favlist = FavList.objects.create(
            user_id=user,
            item_id=item_id
        )
        ser = FavSerilizers(instance=favlist, data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
        return Response(ser.data)

    @registerd_only_pk
    def delete(self, request, pk):
        fav = FavList.objects.filter(id=pk).first()
        fav.delete()
        return Response('Deleted!')


class CreditAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @registerd_only
    def post(self, request):
        user = request.user
        ser = CreditSerialzers(data=request.data)
        if ser.is_valid(raise_exception=True):
            card_number = request.data['card_number']
            password = request.data['password']
            card_type = request.data['card_type']
            credit = CreditCard.objects.create(
                user_id=user,
                password=password,
                card_number=card_number,
                card_type=card_type
            )
            credit.save()
            return Response(ser.data)


class RatingAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @registerd_only_pk
    def post(self, request, pk):
        user = request.user
        item_id = Item.objects.get(id=pk)
        ser = RatingSerialzers(data=request.data)
        if ser.is_valid(raise_exception=True):
            rate = request.data['rate']
            Rate = Rating.objects.create(
                rate=rate,
                user_id=user,
                item_id=item_id
            )

            Rate.save()
            return Response(ser.data)


class QuentityAPI(APIView, PageNumberPagination):
    @worker_only_pk
    def post(self, request, pk):
        item_id = Item.objects.get(id=pk)
        ser = QuentitySerialzers(data=request.data)
        if ser.is_valid(raise_exception=True):
            color = request.data['color']
            size = request.data['size']
            quantity_of_item = request.data['quantity_of_item']
            quentity = Quantity.objects.create(
                item_id=item_id,
                color=color,
                size=size,
                quantity_of_item=quantity_of_item
            )
            quentity.save()
            return Response(ser.data)



class BestsSellAPI(APIView,PageNumberPagination):
    def get(self,request):

        query=SoldItem.objects.select_related('item_id')\
            .values('item_id').annotate(sum_item=Sum('price'))\
            .order_by('-sum_item')

        result = self.paginate_queryset(query, request, view=self)
        return self.get_paginated_response(result)

