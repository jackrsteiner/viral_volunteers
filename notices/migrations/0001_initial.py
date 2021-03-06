# Generated by Django 3.0.4 on 2020-04-14 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import notices.models
import phonenumber_field.modelfields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('postal', models.CharField(blank=True, default='', max_length=5)),
                ('proximity', models.PositiveIntegerField(default=0)),
                ('loc_json', models.TextField(blank=True, default='', editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('idea', 'Idea'), ('appeal', 'Appeal'), ('opportunity', 'Opportunity')], default='idea', max_length=12)),
                ('body', tinymce.models.HTMLField(verbose_name='Content')),
                ('web', models.URLField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=models.SET(notices.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='notices.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('commenter', models.ForeignKey(on_delete=models.SET(notices.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='notices.Notice')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
