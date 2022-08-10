from django.contrib import admin
from django.urls import path,include
from .views import home,lg,about
from . import views
urlpatterns = [
   path('',views.about, name='about'),
    path( 'home/',views.home ,name='home'),
    
    path( 'lg/',views.lg ,name='lg')
]
