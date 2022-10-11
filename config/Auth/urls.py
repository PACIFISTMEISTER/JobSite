from django.urls import path
from .views import LogIn, SignIn, SignInCompany, Profile, LogOut, ShowLikes, PostJob, ProfileUpdate, ShowCompany, \
    ShowResponses

urlpatterns=[
    path('login',LogIn.as_view()),
    path('signin/user',SignIn.as_view()),
    path('signin/company',SignInCompany.as_view()),
    path('profile',Profile.as_view()),
    path('profile/update',ProfileUpdate.as_view()),
    path('logout',LogOut),
    path('likes',ShowLikes.as_view()),
    path('postjob',PostJob.as_view()),
    path('Company',ShowCompany.as_view()),
    path('response',ShowResponses.as_view())
    #path('/logout')
    #path('/signin')
]