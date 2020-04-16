from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='vv_app-home'),
    #path('', views.about, name='vv_app-about'),
    path('about/', views.about, name='vv_app-about'),
]