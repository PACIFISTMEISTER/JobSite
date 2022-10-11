from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Auth.models import ChangeUser, DeleteLike,AddLike,DeleteJob,AddReq,DelRespose
from Auth.protect import DecorForUserLogFunc


@csrf_exempt
@DecorForUserLogFunc
def StatusChange(request,pk):
    ChangeUser(pk)
    return HttpResponse('')

@csrf_exempt
@DecorForUserLogFunc
def Dislike(request,pk):
    DeleteLike(request.user,pk)
    return HttpResponse('')


@csrf_exempt
@DecorForUserLogFunc
def Like(request,pk):
    AddLike(request.user,pk)
    return HttpResponse('')


@csrf_exempt
def Delete(request,pk):
    DeleteJob(pk)
    return HttpResponse('')

@csrf_exempt
@DecorForUserLogFunc
def AddRequest(request,pk):
    AddReq(request.user,pk)
    return HttpResponse('')

@csrf_exempt
@DecorForUserLogFunc
def DeleteRespose(request,pk):
    DelRespose(request.user,pk)
    return HttpResponse('')