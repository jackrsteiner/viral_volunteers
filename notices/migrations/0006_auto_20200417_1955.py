# Generated by Django 3.0.4 on 2020-04-17 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0005_auto_20200415_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='category',
            field=models.CharField(choices=[('idea', 'Idea'), ('appeal', 'Appeal'), ('opportunity', 'Opportunity'), ('service', 'Service')], default='idea', max_length=12),
        ),
    ]
