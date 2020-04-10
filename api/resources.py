from tastypie.resources import ModelResource
from notices.models import Notice
from tastypie.authorization import Authorization

class NoticeResource(ModelResource):
    class Meta:
        queryset = Notice.objects.all()
        resource_name = 'notice'
        authorization = Authorization()