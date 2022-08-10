from django.contrib import admin
from django.urls import path,include
from .views import home,lg
from . import views
urlpatterns = [

    path( '',views.home ,name='home'),
    
    path( 'lg/',views.lg ,name='lg')
]
