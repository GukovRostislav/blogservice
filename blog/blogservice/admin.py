from django.contrib import admin
from .models import Posts
from .forms import AddPostForm


@admin.register(Posts)
class FooAdmin(admin.ModelAdmin):
    form = AddPostForm
