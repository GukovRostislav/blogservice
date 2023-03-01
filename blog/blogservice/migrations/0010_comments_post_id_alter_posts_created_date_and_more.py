# Generated by Django 4.1.7 on 2023-02-23 15:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogservice', '0009_comments_alter_posts_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='post_id',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 15, 46, 14, 560226)),
        ),
        migrations.AlterField(
            model_name='users',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 15, 46, 14, 560226)),
        ),
    ]