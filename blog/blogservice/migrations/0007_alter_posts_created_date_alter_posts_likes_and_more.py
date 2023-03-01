# Generated by Django 4.1.3 on 2023-02-20 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogservice', '0006_posts_preview_alter_posts_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 16, 7, 42, 734366)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='users',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 16, 7, 42, 734366)),
        ),
    ]
