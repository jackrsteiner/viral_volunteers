"""viral_volunteers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from api.resources import NoticeResource
from users import views as user_views
from notices.views import NoticeListView
from . import views

notice_resource = NoticeResource()

urlpatterns = [
    path('', NoticeListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('testing', views.testim, name='testy'),
    path('', include ('vv_app.urls')),
    #path('about/', include('vv_app.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('notices/', include('notices.urls')),
    path('api/', include(notice_resource.urls)),
    path('tinymce/', include('tinymce.urls')),
]
