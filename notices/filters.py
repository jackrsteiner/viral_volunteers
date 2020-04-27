from django_filters import FilterSet, DateFilter, CharFilter, BooleanFilter
from django.forms import CheckboxInput, HiddenInput
from .models import *

class NoticeFilter(FilterSet):
    title = CharFilter(label='Title Keywords',field_name='title',lookup_expr='icontains')
    start_date = DateFilter(label='From Date (mm/dd/yyyy)',field_name="last_modified", lookup_expr='gte')
    end_date = DateFilter(label='Till Date (mm/dd/yyyy)',field_name="last_modified", lookup_expr='lte')
    class Meta:
        model = Notice
        fields = ['category']

class NoticeSearchBarFilter(FilterSet):
   class Meta:
        model = Notice
        fields = ['active','category','title']

class NoticeTableFilter(FilterSet):
   class Meta:
        model = Notice
        fields = ['active','category','title']

class NoticeTableCustomFilter(FilterSet):
    title = CharFilter(label='Title Keywords',field_name='title',lookup_expr='icontains')
    start_date = DateFilter(label='From Date (mm/dd/yyyy)',field_name="last_modified", lookup_expr='gte')
    end_date = DateFilter(label='Till Date (mm/dd/yyyy)',field_name="last_modified", lookup_expr='lte')
    # active = BooleanFilter(label='Only active notices', field_name='active', widget=CheckboxInput)

    class Meta:
        model = Notice
        fields = ['category']