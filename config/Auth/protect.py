from django.http import HttpResponseRedirect

from Auth.models import AverageUser, CompanyUser
from companies.models import Company, Job


def DecorForUserLog(func):
    """контроль доступа"""
    def fnc(self, request, *args, **kwargs):
        res = None
        if request.user.is_authenticated and AverageUser.objects.filter(user=request.user).exists():

                res = func(self, request)

        else:
            res = HttpResponseRedirect('/auth/login')
        return res

    return fnc


def decor(func):
    """контроль доступа для классов"""
    def fnc(self, request, *args, **kwargs):
        res = None
        if request.user.is_authenticated:
            if CompanyUser.objects.filter(user=request.user).exists():
                res = func(self, request)
            else:
                res = HttpResponseRedirect('/auth/signin/company')
        else:
            res = HttpResponseRedirect('/auth/login')
        return res

    return fnc


def Protection(func):
    def fnc(self, request, *args, **kwargs):
        res = None
        if request.user.is_authenticated and CompanyUser.objects.filter(user=request.user).exists():

            if int(request.path.split('/')[3]) in list(Job.objects.values_list('id', flat=True).filter(
                    Company=Company.objects.filter(companyuser__user=request.user).get())):

                res = func(self, request)
            else:
                res = HttpResponseRedirect('/auth/login')

        else:
            res = HttpResponseRedirect('/auth/login')
        return res

    return fnc



def DecorForUserLogFunc(func):
    """контроль доступа Для функций"""
    def fnc(request, *args, **kwargs):
        res = None
        if request.user.is_authenticated and AverageUser.objects.filter(user=request.user).exists():

                res = func(request,**kwargs)

        else:
            res = HttpResponseRedirect('/auth/login')
        return res

    return fnc
