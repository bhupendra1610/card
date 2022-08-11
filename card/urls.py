from django.contrib import admin
from django.urls import path,include
from .views import home,lg,about,logout
from . import views
urlpatterns = [
   path('',views.about, name='about'),
    path( 'home/',views.home ,name='home'),
    path( 'logout/', views.logout ,name= 'logout'),
    path( 'lg/',views.lg ,name='lg')
]
