from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from django.views import View
from django.views.generic import DetailView, ListView

from Auth.models import AverageUser, CompanyUser
from Auth.protect import Protection
from Auth.views import DecorForUserLog, decor
from candidates.models import Candidate
from .models import GetLocation, GetCategory, PopularSearch, PopularCategory, MainJob, TopCompanies, GetJob, Job, \
    AvaliableJobs, CategoryJobs, GetSearch, Company, UpdateJob
from .forms import SearchForm, JobForm


class MainPage(View):
    """основная страница"""
    def get(self, request):
        PopularSrch = PopularSearch()
        PopularCtgr = PopularCategory()
        Jobs = MainJob()
        Comp = TopCompanies()
        for cmp in Comp:
            print(cmp)
        context = {  # 'Category': allCategory, 'Location': allLocations,
            'Popular': PopularSrch, 'PopularCategory': PopularCtgr, 'Jobs': Jobs, 'TopCompanies': Comp}
        return render(request=request, template_name='template/index.html', context=context)


class CategoryView(ListView):
    """вывод всех мест работы в определенной категории"""
    paginate_by = 2
    model = Job

    template_name = 'template/jobs.html'

    def get_queryset(self):
        return CategoryJobs(self.kwargs['name'])


class JobView(View):
    """вывод информации о конкретном месте работы"""
    def get(self, request, pk):
        Job = GetJob(pk)
        context = {'Job': Job}
        return render(request=request, template_name='template/job_details.html', context=context)


class AllJobs(ListView):
    """ вся доступная работа"""
    paginate_by = 2
    model = Job
    template_name = 'template/jobs.html'
    ordering = ['Published']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def post(self, request: WSGIRequest, *args, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['type'])

        return HttpResponseRedirect(redirect_to='/')


class SearchView(ListView):
    """вся доступная работа по фильтру"""
    paginate_by = 2
    model = Job
    template_name = 'template/jobs.html'
    ordering = ['Published']

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')
        location = self.request.GET.get('location')
        category = self.request.GET.get('category')
        experience = self.request.GET.get('experience')
        type = self.request.GET.get('type')


        return GetSearch(keyword, location, category, experience, type)





class ShowResponse(ListView, LoginRequiredMixin):
    """отображение вакансии для работодателя"""
    login_url = '/auth/login'
    template_name = 'template/vacancy.html'
    paginate_by = 5

    def get_queryset(self):


        return Candidate.objects.filter(averageuser__Responses=Job.objects.filter(id=self.kwargs['pk']).get())

        #return AverageUser.objects.get(Responses=Job.objects.filter(id=self.kwargs['pk']).get()).Can

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['Job'] = Job.objects.filter(id=self.kwargs['pk']).first()
        return data

    @Protection
    def get(self, request, *args, **kwargs):
        return super().get(self, request, args, kwargs)

    @Protection
    def post(self, request: WSGIRequest, *args, **kwargs):
        form = JobForm(request.POST)
        if form.is_valid():
            UpdateJob(form, request, self.kwargs['pk'])
        return HttpResponseRedirect(self.request.path_info)


def ShowContact(request):
    """контакты"""
    return render(request,template_name='template/contact.html')
