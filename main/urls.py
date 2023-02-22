from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('private_cab', views.about, name='about')
]
