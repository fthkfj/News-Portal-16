# Generated by Django 4.0.4 on 2022-07-29 19:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(related_name='subscribers', to=settings.AUTH_USER_MODEL),
        ),
    ]
