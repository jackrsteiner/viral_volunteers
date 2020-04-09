from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=30)
    CATEGORY_CHOICES = [
        ('idea', 'Idea'),
        ('appeal', 'Appeal'),
        ('opportunity', 'Opportunity'),
    ]
    category = models.CharField(max_length=12,choices=CATEGORY_CHOICES, default='idea')
    postal = models.CharField(max_length=5, default='')
    proximity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return 'Id-%s - %s' % (self.id, self.title)

