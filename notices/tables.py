import django_tables2 as tables
from .models import Notice

class NoticeTable(tables.Table):
    class Meta:
        model = Notice
        template_name = "django_tables2/bootstrap4.html"
        fields = ('active', 'last_modified', 'category', 'title', 'country', 'province')

class NoticeTableCustom(tables.Table):
    class Meta:
        model = Notice
        order_by = ('-last_modified')
        template_name = "django_tables2/bootstrap4.html"
        fields = ('active', 'last_modified', 'category', 'title', 'country', 'province')
        attrs = {"class": "table table-sm table-striped table-bordered"}
        row_attrs = {'class':'ft-row', 'data-href': lambda record: record.get_absolute_url}