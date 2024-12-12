from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Post

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
