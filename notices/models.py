from django.db import models
#from django.utils import timezone
from django.contrib.auth.models import User
from tinymce import HTMLField
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
import geocoder

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted_user')[0]

def get_json(self):
    g = geocoder.osm(self.country + ', ' + self.postal)
    return g.json

# class Contact(models.Model):
#     label = models.CharField(max_length=20)
#     link = models.URLField(blank=True)
#     email = models.EmailField(blank=True)
#     phone = PhoneNumberField(blank=True)

#     def __str__(self):
#         return '%s - %s %s %s' % (self.label, self.link, self.email, self.phone)
#     pass

# class Location(models.Model):
#     country = CountryField()
#     postal = models.CharField(max_length=5, default='', blank=True)
#     proximity = models.PositiveIntegerField(default=0)
#     loc_json = models.TextField(editable=False, default='', blank=True)
    
#     def __str__(self):
#         return 'within %s miles of %s-%s' % (self.proximity, self.postal, self.country)
#     pass

class Notice(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(verbose_name='Modified', auto_now=True)
    CATEGORY_CHOICES = [
        ('idea', 'Idea'),
        ('appeal', 'Appeal'),
        ('opportunity', 'Opportunity'),
        ('service', 'Service')
    ]
    category = models.CharField(max_length=12,choices=CATEGORY_CHOICES, default='idea')
    body = HTMLField()
    #contact = models.ForeignKey(Contact, on_delete=models.CASCADE, default=1)
    web = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField(blank=True)
    country = CountryField(default='', blank=True)
    province = models.CharField(verbose_name='Province or State', max_length=100, default='', blank=True)
    postal = models.CharField(max_length=10, default='', blank=True)
    #location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1, blank=True)
    active = models.BooleanField(default=True)
    approved = models.BooleanField(default=True)
    # comments -- needs to be some other model/foreignkey

    def __str__(self):
        return 'Id:%s - %s' % (self.id, self.title)
    
    def get_absolute_url(self):
        return reverse('notices-notice_detail', kwargs={'pk': self.pk})

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