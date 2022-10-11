from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin

from .forms import Login, SignUser, CompUser, AddResume, UpdateResume, AddJob
from .models import CompanyUser, AverageUser, UpgradeAvg
from companies.models import Company, Job, Location, Category
from candidates.models import Candidate

# Create your views here.
from django.views import View

from .protect import DecorForUserLog, decor


class LogIn(View):
    """логин вью"""
    def get(self, request):

        return render(request=request, template_name='template/Login.html')

    def post(self, request: WSGIRequest):
        form = Login(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['login'], password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(redirect_to='/')
            else:
                return HttpResponseRedirect(redirect_to='/auth/login/user')
        else:
            return HttpResponseRedirect(redirect_to='/auth/login/user')


class SignIn(View):
    """регистрация"""
    def get(self, request):

        return render(request=request, template_name='template/SignIn.html')

    def post(self, request: WSGIRequest):
        form = SignUser(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                user = User.objects.create_user(username=form.cleaned_data['login'],
                                                password=form.cleaned_data['password1'],
                                                email=form.cleaned_data['email'], first_name=form.cleaned_data['name'],
                                                last_name=form.cleaned_data['surname'])
                avg = AverageUser(user=user)
                avg.save()
                user.save()

                login(request, user)
                return HttpResponseRedirect(redirect_to='/')
            else:
                return HttpResponseRedirect(redirect_to='/auth/signin/user')

        else:
            return HttpResponseRedirect(redirect_to='/auth/signin/user')


class SignInCompany(View):
    """регитсрация для компнаий"""
    def get(self, request: WSGIRequest):
        return render(request=request, template_name='template/CompanySignIn.html')

    def post(self, request: WSGIRequest):
        form = CompUser(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                user = User.objects.create_user(username=form.cleaned_data['login'],
                                                password=form.cleaned_data['password1'],
                                                email=form.cleaned_data['email'], first_name=form.cleaned_data['name'],
                                                last_name=form.cleaned_data['surname'])

                comp = Company(Name=form.cleaned_data['companyname'], Symbol=form.cleaned_data['img'],
                               CNN=form.cleaned_data['CNN'],
                               SomeInfo=form.cleaned_data['info'])
                comp.save()

                cmp = CompanyUser(user=user, company=comp)

                user.save()
                login(request, user)
                cmp.save()
                return HttpResponseRedirect(redirect_to='/')
            else:
                return HttpResponseRedirect(redirect_to='/job')
        else:
            return HttpResponseRedirect(redirect_to='/auth/signin/company')


class Profile(LoginRequiredMixin, View):
    """профиль"""
    login_url = '/auth/login'

    def get(self, request):
        return render(request, template_name='template/profile.html')

    def post(self, request: WSGIRequest):
        form = AddResume(request.POST, request.FILES)

        if form.is_valid():
            can = Candidate(Name=form.cleaned_data['Name'], Surname=form.cleaned_data['Surname'],
                            Education=form.cleaned_data['Education'], Expirience=form.cleaned_data['Expirience'],
                            Resume=form.cleaned_data['Resume'], Mail=form.cleaned_data['Mail'],
                            Photo=form.cleaned_data['Photo'], Position=form.cleaned_data['Position'],
                            ShortInfo=form.cleaned_data['ShortInfo'], Qualifications=form.cleaned_data['Qualification'])
            can.save()
            UpgradeAvg(request.user, can)

            return HttpResponseRedirect('/job')
        return HttpResponseRedirect('/')


def LogOut(request):
    """логаут"""
    logout(request)
    return HttpResponseRedirect('/')


class ShowLikes(ListView, LoginRequiredMixin):
    """отображение лайков"""
    login_url = '/auth/login'
    template_name = 'template/LikedJobs.html'
    paginate_by = 5

    def get_queryset(self):
        return AverageUser.objects.get(user=self.request.user).Liked.all()

    @DecorForUserLog
    def get(self, request, *args, **kwargs):
        return super().get(self, request, args, kwargs)





class PostJob(View):
    """добавление работы"""

    @decor
    def get(self, request):
        return render(request=request, template_name='template/AddJob.html')

    @decor
    def post(self, request):

        form = AddJob(request.POST)

        if form.is_valid():
            job = Job(
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
            job.save()
            return HttpResponseRedirect('/job')
        return HttpResponseRedirect('/')


class ProfileUpdate(View):
    """обновление профиля"""

    def post(self, request: WSGIRequest):

        form = UpdateResume(request.POST, request.FILES)

        if form.is_valid():
            Resume = request.FILES.get('Resume', False)
            Photo = request.FILES.get('Photo', False)

            if Resume and Photo:
                can = Candidate.objects.filter(averageuser__user=request.user).first()
                can.Name = form.cleaned_data['Name']
                can.Surname = form.cleaned_data['Surname']
                can.Education = form.cleaned_data['Education']
                can.Expirience = form.cleaned_data['Expirience']
                can.Mail = form.cleaned_data['Mail']
                can.Position = form.cleaned_data['Position']
                can.ShortInfo = form.cleaned_data['ShortInfo']
                can.Qualifications = form.cleaned_data['Qualification']
                can.Resume = form.cleaned_data['Resume']
                can.Photo = form.cleaned_data['Photo']
                can.save()
            elif Resume:
                can = Candidate.objects.filter(averageuser__user=request.user).first()
                can.Name = form.cleaned_data['Name']
                can.Surname = form.cleaned_data['Surname']
                can.Education = form.cleaned_data['Education']
                can.Expirience = form.cleaned_data['Expirience']
                can.Mail = form.cleaned_data['Mail']
                can.Position = form.cleaned_data['Position']
                can.ShortInfo = form.cleaned_data['ShortInfo']
                can.Qualifications = form.cleaned_data['Qualification']
                can.Resume = form.cleaned_data['Resume']
                can.save()
            elif Photo:
                can = Candidate.objects.filter(averageuser__user=request.user).first()
                can.Name = form.cleaned_data['Name']
                can.Surname = form.cleaned_data['Surname']
                can.Education = form.cleaned_data['Education']
                can.Expirience = form.cleaned_data['Expirience']
                can.Mail = form.cleaned_data['Mail']
                can.Position = form.cleaned_data['Position']
                can.ShortInfo = form.cleaned_data['ShortInfo']
                can.Qualifications = form.cleaned_data['Qualification']
                can.Photo = form.cleaned_data['Photo']
                can.save()
                return HttpResponseRedirect('/')

        return HttpResponseRedirect('/job')


class ShowCompany(ListView):
    """отображение информации о компании"""
    template_name = 'template/Company.html'
    paginate_by = 10

    def get_queryset(self):
        return Job.objects.filter(Company=self.request.user.companyuser.company)

    @decor
    def get(self, request, *args, **kwargs):
        return super().get(self, request, args, kwargs)


class ShowVacancy(ListView):
    """отображение вакансий"""
    template_name = 'templates/vacancy.html'
    paginate_by = 5



class ShowResponses(ListView, LoginRequiredMixin):
    """отображение откликов"""
    login_url = '/auth/login'
    template_name = 'template/Responses.html'
    paginate_by = 5

    def get_queryset(self):
        return AverageUser.objects.get(user=self.request.user).Responses.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

    @DecorForUserLog
    def get(self, request, *args, **kwargs):
        return super().get(self, request, args, kwargs)











