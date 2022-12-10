from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  
    path('readmore/<str:slug>/', views.readmore, name='readmore'), 
    path('about', views.about, name ='about'),
    path('stories', views.others, name = "stories")
]
