from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.response import Response
from .models import CustomeUser


def registerd_only(func):
    def warp(self,request):
        if request.user.is_registered==True:
            return func(self,request)
        else:
            return Response('UNAUTHORIZED')
    return warp

def registerd_only_pk(func):
    def warp(self,request,pk):
        if request.user.is_registered==True:
            return func(self,request,pk)
        else:
            return Response('UNAUTHORIZED')
    return warp

def worker_only(func):
    def warp(self,request):
        if request.user.is_worker==True:
            return func(self,request)
        else:
            return Response('UNAUTHORIZED')
    return warp

def worker_only_pk(func):
    def warp(self,request,pk):
        if request.user.is_worker==True:
            return func(self,request,pk)
        else:
            return Response('UNAUTHORIZED')
    return warp


def is_auth(func):
    def warp(self,request):
        if request.user.is_authenticated:
          return func(self,request)
        else:
            return Response( "Your not worker!",status=status.HTTP_401_UNAUTHORIZED)
    return warp

def is_auth_pk(func):
    def warp(self,request,pk):
        if request.user.is_authenticated:
          return func(self,request)
        else:
            return Response( "Your not worker!",status=status.HTTP_401_UNAUTHORIZED)
    return warp