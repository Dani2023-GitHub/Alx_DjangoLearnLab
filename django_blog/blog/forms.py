from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Post, Comment
from taggit.forms import TagField, TagWidget

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginLorm(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs = {'autofocus':True}))
    password  = forms.CharField(label = _('Password'), strip = False,
                widget = forms.PasswordInput(attrs={'autocomplete':'current-password'}))
    
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'published_date', 'author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class PostForm(forms.ModelForm):
    tags = TagField(
        required=False,
        widget=TagWidget()
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
