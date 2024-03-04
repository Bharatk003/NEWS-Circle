# forms.py
from django import forms
from .models import Comment,Article

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',  ]
        # Exclude the article field if it's set in the view.


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'post_img']
