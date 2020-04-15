from django.urls import path
from .views import (
    NoticeListView,
    NoticeDetailView,
    NoticeCreateView,
    NoticeUpdateView,
    NoticeTableView,
    NoticeTableViewHome,
    UserNoticeListView
)
from . import views

urlpatterns = [
    #path('home/', , name='notices-home'),
#    path('about/', views.about, name='notices-about'),
    path('', NoticeListView.as_view(), name='notices-notice_list'),
#    path('', views.notice_list, name='notices-notice_list'),
    path('<int:pk>/', NoticeDetailView.as_view(), name='notices-notice_detail'),
    path('new/', NoticeCreateView.as_view(), name='notices-notice_create'),
    path('<int:pk>/edit/', NoticeUpdateView.as_view(), name='notices-edit'),
    path('table/', NoticeTableView.as_view(), name='notices-table'),
    path('table/home', NoticeTableViewHome.as_view()),
    path('user/<str:username>', UserNoticeListView.as_view(), name='user-notice_list'),

]