from django.db import models
from django import forms
from . models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
    body = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        "class": "textarea", "rows": 3, "cols": 30, "placeholder": " Share your thoughts..."
    }))
    class Meta:
        model = Comment
        fields = ['body']



#REGISTRATION
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"Placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))

    class Meta:
        model = User
        fields = ['username','email']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.username = instance.email
        if commit:
            instance.save()
        return instance     

   
