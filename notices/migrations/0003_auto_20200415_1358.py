# Generated by Django 3.0.4 on 2020-04-15 13:58

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_auto_20200414_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='location',
        ),
        migrations.AddField(
            model_name='notice',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default='', max_length=2),
        ),
        migrations.AddField(
            model_name='notice',
            name='postal',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AddField(
            model_name='notice',
            name='state',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
