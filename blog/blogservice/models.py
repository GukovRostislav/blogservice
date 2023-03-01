from django.db import models
from django.utils.timezone import now


class Users(models.Model):
    email = models.TextField()
    login = models.TextField()
    password = models.TextField()
    join_date = models.DateTimeField(default=now())


class Posts(models.Model):
    title = models.TextField()
    post_author_id = models.IntegerField()
    content = models.TextField()
    likes = models.IntegerField(default=0)
    post_views = models.IntegerField(default=0)
    preview = models.ImageField(blank=True, upload_to='previews')
    created_date = models.DateTimeField(default=now())


class Likes(models.Model):
    user_id = models.IntegerField()
    post_id = models.IntegerField()


class Comments(models.Model):
    content = models.TextField()
    author = models.TextField()
    post_id = models.IntegerField()
