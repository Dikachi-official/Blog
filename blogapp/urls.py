from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='home'),  
    path('readmore/<str:slug>/', views.readmore, name='readmore'), 
    path('about', views.about, name ='about'),
    path('stories', views.others, name = "stories"),

    #LOGIN AND LOGOUT ROUTE
    path('signup', views.register_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]
