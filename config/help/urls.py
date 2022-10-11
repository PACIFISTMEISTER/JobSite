from django.urls import path
from .views import StatusChange, Dislike, Like, Delete,AddRequest,DeleteRespose

urlpatterns=[
    path('StatusChange/<int:pk>',StatusChange),
    path('Dislike/<int:pk>',Dislike),
    path('Like/<int:pk>',Like),
    path('Delete/<int:pk>',Delete),
    path('AddToRequest/<int:pk>',AddRequest),
    path('DeleteResponse/<int:pk>',DeleteRespose)
]
