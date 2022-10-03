from django.urls import path
from . import views
urlpatterns = [
    path('api/user/',views.User.as_view(),name='user'),
    path('api/login/',views.login.as_view(),name='login'),
   ]