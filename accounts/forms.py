from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Signup Form
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'input-class', 'placeholder': 'Email'
    }))
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'input-class', 'placeholder': 'Bio', 'rows': 3
    }), required=False)
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'bio', 'profile_image']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.bio = self.cleaned_data['bio']
        if self.cleaned_data.get('profile_image'):
            user.profile_image = self.cleaned_data['profile_image']

        if commit:
            user.save()
        return user

# Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-class', 'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-class', 'placeholder': 'Password'
    }))
