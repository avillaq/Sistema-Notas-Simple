from django.contrib import admin
from django.urls import path
from sistema import views 

urlpatterns = [
    path('', view=views.index, name='index'),
]
