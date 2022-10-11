from django.urls import path
from django.views.decorators.cache import cache_page

from .views import MainPage, CategoryView, JobView, AllJobs, SearchView, ShowResponse,ShowContact

urlpatterns = [
    path('',cache_page(60 * 15)( MainPage.as_view())),
    path('job', AllJobs.as_view()),
path('contact',ShowContact),
    path('job/<int:pk>', JobView.as_view(), name='jobdetail'),
    path('job/<slug:search>', SearchView.as_view()),
    path('category/<str:name>', CategoryView.as_view(), name='category'),
    path('Info/job/<int:pk>', ShowResponse.as_view()),
    #path('Info/job/<int:pk>/Change', ShowResponse.as_view())
]
