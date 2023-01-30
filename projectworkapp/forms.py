from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,SetPasswordForm,PasswordResetForm
from django.contrib.auth.models import User
from django.utils import timezone
from .models import upload_file

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class SubmitForm(forms.Form):  
    #firstname = forms.CharField(label="Enter first name",max_length=50)  
    #lastname  = forms.CharField(label="Enter last name", max_length = 10)  
    #email     = forms.EmailField(label="Enter Email")
    file_name =  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    files_data = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'})) # for creating file input

