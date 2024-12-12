from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Post

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='password', widget=forms.
                PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="confirm password", widget=forms.
                PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'username':'user name', 'first_name': 'first name', 'last_name': 'last name', 
                   'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                   'first_name':forms.TextInput(attrs = {'class':'form-control'}),
                   'last_name':forms.TextInput(attrs = {'class':'form-control'}),
                   'email':forms.EmailInput(attrs = {'class':'form-control'}),
                   }
        
class LoginLorm(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs = {'autofocus':True}))
    password  = forms.CharField(label = _('Password'), strip = False,
                widget = forms.PasswordInput(attrs={'autocomplete':'current-password'}))
    
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'published_date', 'author']
