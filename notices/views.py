from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
from notices.forms import NoticeCreateForm
from notices.models import Notice
from django_tables2 import SingleTableView
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from .tables import NoticeTable, NoticeTableCustom
from .filters import NoticeFilter, NoticeTableFilter, NoticeTableCustomFilter

def notice_search_table(request):
    notices = Notice.objects.all()
    myFilter = NoticeFilter(request.GET, queryset=notices)
    notices = myFilter.qs

    context = {
        'notices': notices, 'myFilter': myFilter
    }
    return render(request, 'notices/notice_functable.html', context)


def notice_search(request):
    notices = Notice.objects.all()
    myFilter = NoticeFilter(request.GET, queryset=notices)
    notices = myFilter.qs

    context = {
        'notices': notices, 'myFilter': myFilter
    }
    return render(request, 'notices/notice_functable.html', context)

class NoticeListView(ListView):
    model = Notice
    template_name = 'notices/notice_list.html' # default is <app>/<model>_<viewtype>.html
    context_object_name = 'notices'
    ordering = ['-last_modified']
    paginate_by = 5

class NoticeTableViewHome(SingleTableView):
    model = Notice
    table_class = NoticeTable
    template_name = 'notices/table.html'

class UserNoticeListView(ListView):
    model = Notice
    template_name = 'notices/user_notices.html' # default is <app>/<model>_<viewtype>.html
    context_object_name = 'notices'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Notice.objects.filter(author=user).order_by('-last_modified')

class NoticeDetailView(DetailView):
    model = Notice

class NoticeCreateView(LoginRequiredMixin, CreateView):
    model = Notice
    form_class = NoticeCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NoticeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notice
    fields = ['title', 'category', 'body', 'web', 'email', 'phone', 'country', 'province', 'postal', 'active']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        notice = self.get_object()
        if self.request.user == notice.author:
            return True
        return False

class NoticeTableView(ListView):
    model = Notice
    template_name = 'notices/notice_table.html'
    filterset_class = NoticeTableFilter

# class NoticeTableView(SingleTableView):
#     model = Notice
#     table_class = NoticeTable
#     filterset_class = NoticeFilter
#     template_name = 'notices/notice_table.html'
#     myFilter = NoticeFilter()
#     queryset = Notice.objects.filter(category='opportunity')
#     def get_queryset(self):
#         qs = Notice.objects.all()
#         notice_filtered_list = NoticeFilter(self.request.GET, queryset=qs)
#         return notice_filtered_list.qs

# class NoticeTableView(SingleTableView):
#     model = Notice
#     table_class = NoticeTable
#     template_name = 'notices/table_old.html'

class FilteredTableView(SingleTableMixin, FilterView):
    table_class = NoticeTableCustom
    model = Notice
    template_name = "notices/tablefiltered.html"

    filterset_class = NoticeTableCustomFilter
    table_pagination = {"per_page": 10}