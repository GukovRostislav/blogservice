from django.forms import ModelForm, Textarea
from .models import Posts, Comments


class AddPostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'preview', 'content', ]
        widgets = {
            'title': Textarea(attrs={'cols': 50, 'rows': 1}),
        }


class AddCommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['content', ]
        widgets = {
            'content': Textarea(attrs={"maxlength": "500"}),
        }
