# Generated by Django 5.1.6 on 2025-03-19 16:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_landrequesthistory_remove_landapplication_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='landrequest',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
