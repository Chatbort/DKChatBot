#### django imports ####
from django.urls import path

#### our app imports ####
from app import views

#### others ####

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]
