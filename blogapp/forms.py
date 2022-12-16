from django.db import models
from django import forms
from . models import Comment


class CommentForm(forms.ModelForm):
    body = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        "class": "textarea", "rows": 3, "cols": 30, "placeholder": " Share your thoughts..."
    }))
    class Meta:
        model = Comment
        fields = ['body']
