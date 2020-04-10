from django.db import models
#from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted_user')[0]

class Notice(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    CATEGORY_CHOICES = [
        ('idea', 'Idea'),
        ('appeal', 'Appeal'),
        ('opportunity', 'Opportunity'),
    ]
    category = models.CharField(max_length=12,choices=CATEGORY_CHOICES, default='idea')
    body = models.TextField()
    info_link = models.URLField(blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = PhoneNumberField(blank=True)
    postal = models.CharField(max_length=5, default='')
    country = CountryField()
    proximity = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    # comments -- needs to be some other model/foreignkey

    def __str__(self):
        return 'Id:%s - %s' % (self.id, self.title)