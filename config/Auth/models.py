from django.contrib.auth.models import User
from django.db import models
from django.db.models import Case, Value, When

from companies.models import Company,Job
from candidates.models import Candidate


class CompanyUser(models.Model):
    """hr"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.OneToOneField(Company, on_delete=models.CASCADE, default=5)
    Liked = models.ManyToManyField(Candidate)


    def __str__(self):
        return self.user.username


class AverageUser(models.Model):
    """соискатель"""
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    Candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE,null=True,blank=True)
    Liked = models.ManyToManyField(Job,null=True,blank=True)
    isCandidate = models.BooleanField(default=False)
    Responses = models.ManyToManyField(Job,related_name='responses')



    def __str__(self):
        return self.user.username


def GetAllCandidates():
    """возвращает всех кандидат"""
    return Candidate.objects.filter(averageuser__isCandidate=True)



def ChangeUser(pk):
    """изменеие статуса поиска работы у соискателя"""
    AverageUser.objects.filter(id=pk).update(isCandidate=Case(
        When(isCandidate=True,then=Value(False)),
        When(isCandidate=False, then=Value(True)),
    ))

def UpgradeAvg(User,Candidate):
    """обновление соискатлея"""
    AverageUser.objects.filter(user=User).update(Candidate=Candidate)


def DeleteLike(User,pk):
    """убирает лайк"""
    AverageUser.objects.filter(user=User).get().Liked.remove(Job.objects.filter(id=pk).get())


def AddLike(User,pk):
    """добавляет лайк"""
    AverageUser.objects.filter(user=User).get().Liked.add(Job.objects.filter(id=pk).get())

def DeleteJob(pk):
    """удаление работы по ключу"""
    Job.objects.filter(id=pk).delete()


def AddReq(User,pk):
    """добавляет отклик"""
    AverageUser.objects.filter(user=User).get().Responses.add(Job.objects.filter(id=pk).get())


def DelRespose(User,pk):
    """удаляет отклик"""
    AverageUser.objects.filter(user=User).get().Responses.remove(Job.objects.filter(id=pk).get())





