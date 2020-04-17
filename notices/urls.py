from django.urls import path
from .views import (
    NoticeListView,
    NoticeDetailView,
    NoticeCreateView,
    NoticeUpdateView,
    NoticeTableViewHome,
    UserNoticeListView,
    NoticeFilter,
    NoticeTableView

)
from notices import views
from django_filters.views import FilterView
from .filters import NoticeTableFilter

urlpatterns = [
    #path('home/', , name='notices-home'),
#    path('about/', views.about, name='notices-about'),
    path('', NoticeListView.as_view(), name='notices-notice_list'),
    path('search/', views.notice_search, name='notice_functable'),
    path('<int:pk>/', NoticeDetailView.as_view(), name='notices-notice_detail'),
    path('new/', NoticeCreateView.as_view(), name='notices-notice_create'),
    path('<int:pk>/edit/', NoticeUpdateView.as_view(), name='notices-edit'),
    path('table/home', NoticeTableViewHome.as_view()),
    path('user/<str:username>', UserNoticeListView.as_view(), name='user-notice_list'),

    path('table/', NoticeTableView.as_view(
        template_name='notices/notice_table.html'), name='notices-table'),

]