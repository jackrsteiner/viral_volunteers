from django.db import models
#from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
import geocoder

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted_user')[0]

def get_json(self):
    g = geocoder.osm(self.country + ', ' + self.postal)
    return g.json

class Contact(models.Model):
    label = models.CharField(max_length=20)
    link = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField(blank=True)

    def __str__(self):
        return 'id#%s - %s' % (self.id, self.label)
    pass

class Location(models.Model):
    country = CountryField()
    postal = models.CharField(max_length=5, default='')
    proximity = models.PositiveIntegerField(default=0)
    loc_json = models.TextField(editable=False, default=get_json)

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
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, default=1)
    info_link = models.URLField(blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = PhoneNumberField(blank=True)
    active = models.BooleanField(default=True)
    # comments -- needs to be some other model/foreignkey

    def __str__(self):
        return 'Id:%s - %s' % (self.id, self.title)

class Comment(models.Model):
    notice = models.ForeignKey(Notice,on_delete=models.CASCADE,related_name='comments')
    title = models.CharField(max_length=80)
    commenter = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.commenter)