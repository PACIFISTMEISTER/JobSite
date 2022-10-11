from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import QuerySet, F
from django.urls import reverse



class MainManager(models.Manager):
    """мэнеджер для вывода компаний, которые должны быть на главном экране"""
    def get_queryset(self):
        return super().get_queryset().filter(IsOnMain=True)


class Category(models.Model):
    """инофрмация о категории"""
    Name = models.TextField(max_length=50, default='unnamed', unique=True)
    Requests = models.IntegerField(null=True)
    AvalibleJob = models.IntegerField(default=0)

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('category', kwargs={'name': self.Name})

    class Meta:
        ordering =['Name']


class Location(models.Model):
    """инофрмация о месте"""
    Name = models.TextField(default='unknown')
    X = models.IntegerField(default=1)
    Y = models.IntegerField(default=1)

    def __str__(self):
        return self.Name


class Company(models.Model):
    """информация о компании"""

    class RatingChoices(models.IntegerChoices):
        Awful = 1
        Bad = 2
        Better = 3
        Good = 4
        Best = 5

    Name = models.TextField(default='unknown')
    Rating = models.IntegerField(choices=RatingChoices.choices, default=0)
    Symbol = models.ImageField(null=True, upload_to='media')
    CNN=models.TextField(default='hi')
    SomeInfo=models.TextField(default='hello')

    class Meta:
        ordering =['Name']


    def __str__(self):
        return self.Name


class Job(models.Model):
    """описание предложения и компании"""

    class CategoryChoices(models.TextChoices):
        part_time = 'part_time'
        full_time = 'full_time'

    class ExpChoices(models.TextChoices):
        Any = 'Any'
        junior = 'Junior'
        middle = 'Middle'
        senior = 'Senior'

    Name = models.TextField(max_length=20)
    Type = models.TextField(choices=CategoryChoices.choices)
    Description = models.TextField(max_length=500)
    Responsibilities = models.TextField()
    Qualifications = models.TextField()
    Benefits = models.TextField(max_length=500)
    Email = models.EmailField()
    Published = models.DateField(auto_now=True)
    Min_salary = models.PositiveSmallIntegerField()
    Max_salary = models.PositiveSmallIntegerField()
    Location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    IsOnMain = models.BooleanField(default=False)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    Exp = models.TextField(choices=ExpChoices.choices, default='Junior')

    class Meta:
        ordering =['Name']

    objects = models.Manager()
    main_object = MainManager()

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        name = self.Name.replace(' ', '')
        return reverse('jobdetail', kwargs={'pk': self.id})


def GetLocation() -> QuerySet:
    """возвращает имена всех мест"""
    return Location.objects.all().only('Name')


def GetCategory() -> QuerySet:
    """возвращает имена всех категорий"""
    return Category.objects.all().only('Name')


def PopularSearch() -> QuerySet:
    """возвращает 5 самых популярные категории по запросам"""
    return Category.objects.order_by('Requests').only('Name')[:5]


def PopularCategory() -> QuerySet:
    """возвращает 5 самых популярные категории по доступным работам"""
    return Category.objects.order_by('-AvalibleJob')[:8]


def MainJob() -> QuerySet:
    """возвращает все, что связано с доступными работами на основной старнице"""
    return Job.main_object.all().select_related()


def TopCompanies() -> QuerySet:
    """возвращает топ 4 компании по рейтингу"""
    return Company.objects.raw(""" select   comp."id", count(job."Name") from companies_company as comp 
join companies_job as job on comp.Id=job."Company_id" group by comp."id" order by comp."id" limit 4 """)
    #return Company.objects.order_by('-Rating')[:4]


def GetJob(pk: str):
    """возвращает всю необходимую информацию посвященную работе"""
    return Job.objects.filter(id=pk).select_related()


def AvaliableJobs():
    """возвращает все доступные места занятости"""
    return Job.objects.all().count()


def CategoryJobs(name: str):
    """возвращает все доступые места занятости по категории"""
    return Job.objects.filter(Category__Name=name)


def GetSearch(keyword=None, location=None, category=None, experience=None, type=None):
    """фильтрация по поиску"""
    Category.objects.filter(Name=category).update(Requests=F('Requests') + 1)
    if experience and type:
        if keyword:

            return Job.objects.filter(Name__icontains=keyword, Location__Name=location, Category__Name=category, Exp=experience,
                                    Type=type)
        else:
            return Job.objects.filter(Location__Name=location, Category__Name=category, Exp=experience,
                                    Type=type)
    else:
        if keyword:
            return Job.objects.filter(Name__icontains=keyword, Location__Name=location, Category__Name=category,)
        else:
            return Job.objects.filter(Location__Name=location, Category__Name=category)


def UpdateJob(form,request,pk):
    """обновление работы"""
    Job.objects.filter(id=pk).update(
        Name=form.cleaned_data['Name'],
        Type=form.cleaned_data['Type'],
        Description=form.cleaned_data['Description'],
        Responsibilities=form.cleaned_data['Responsibilities'],
        Qualifications=form.cleaned_data['Qualifications'],
        Benefits=form.cleaned_data['Benefits'],
        Email=form.cleaned_data['Email'],
        Min_salary=form.cleaned_data['Min'],
        Max_salary=form.cleaned_data['Max'],
        Location=Location.objects.filter(Name=form.cleaned_data['Location']).first(),
        Category=Category.objects.filter(Name=form.cleaned_data['Category']).first(),
        Company=request.user.companyuser.company,
        Exp=form.cleaned_data['Experience'],
    )



