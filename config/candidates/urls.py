from django.urls import path

from .views import ShowAll, ShowCandidate

urlpatterns=[
    path('',ShowAll.as_view()),
    path('<int:pk>', ShowCandidate.as_view(),name='candidateInfo')
]
