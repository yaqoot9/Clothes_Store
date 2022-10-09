from django.urls import path
from . import views

urlpatterns = [
    path('api/user/', views.User.as_view(), name='user'),
    path('api/login/', views.login.as_view(), name='login'),
    path('api/items/<name>/<category>/<gender>/<price>/', views.ItemAPI.as_view(), name='ListItem'),
    path('api/item/',views.ItemAPI.as_view(),name='Item'),
    path('api/item/<str:pk>/',views.ItemAPI.as_view(),name='Item1'),
    path('api/fav/<pk>/',views.FavListAPI.as_view(),name='FavList'),
    path('api/Buy/<pk>/', views.BuyItem.as_view(), name='BuyItem'),
    path('api/credit/', views.CreditAPI.as_view(), name='credit'),
    path('api/Rating/<pk>/', views.RatingAPI.as_view(), name='Rating'),
    path('api/quentity/<pk>/', views.QuentityAPI.as_view(), name='Quentity'),
    path('api/best/', views.BestsSellAPI.as_view(), name='BestSeller'),
]