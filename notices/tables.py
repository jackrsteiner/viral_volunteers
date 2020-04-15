import django_tables2 as tables
from .models import Notice

class NoticeTable(tables.Table):
    class Meta:
        model = Notice
        fields = ('active', 'last_modified', 'category', 'title', 'country', 'province')