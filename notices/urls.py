from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='notices-home'),
    path('about/', views.about, name='notices-about'),
]