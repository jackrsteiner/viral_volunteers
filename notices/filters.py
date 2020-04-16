from django_filters import FilterSet
from django_filters import DateFilter, CharFilter
from .models import *

class NoticeFilter(FilterSet):
    start_date = DateFilter(field_name="last_modified", lookup_expr='gte')
    end_date = DateFilter(field_name="last_modified", lookup_expr='lte')
    title = CharFilter(field_name='title',lookup_expr='icontains')
    class Meta:
        model = Notice
        fields = ['active','category','title','country','province','last_modified']

class NoticeSearchBarFilter(FilterSet):
   class Meta:
        model = Notice
        fields = ['active','category','title']