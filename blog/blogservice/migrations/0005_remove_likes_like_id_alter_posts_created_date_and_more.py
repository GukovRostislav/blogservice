# Generated by Django 4.1.6 on 2023-02-09 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogservice', '0004_likes_alter_posts_created_date_alter_users_join_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='like_id',
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 9, 15, 19, 56, 44119)),
        ),
        migrations.AlterField(
            model_name='users',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 9, 15, 19, 56, 44119)),
        ),
    ]
