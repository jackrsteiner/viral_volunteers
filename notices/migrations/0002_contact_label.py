# Generated by Django 3.0.4 on 2020-04-11 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='label',
            field=models.CharField(default='Registration', max_length=20),
            preserve_default=False,
        ),
    ]
