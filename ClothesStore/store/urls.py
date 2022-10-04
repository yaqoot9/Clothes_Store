from django.urls import path
from . import views

urlpatterns = [
    path('api/user/', views.User.as_view(), name='user'),
    path('api/login/', views.login.as_view(), name='login'),
    path('api/items/<name>/<category>/<gender>/<str:price>/', views.ListItem.as_view(), name='ListItem'),
    path('api/item/',views.ItemAPI.as_view(),name='Item'),
    path('api/item/<str:pk>/',views.ItemAPI.as_view(),name='Item1'),
]
