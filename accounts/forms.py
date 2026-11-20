from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = [
            'full_name',
            'bio',
            'skills',
            'github_url',
            'linkedin_url',
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
            }),

            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us about yourself',
                'rows': 3,
            }),

            'skills': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Python, Django, SQL...',
            }),

            'github_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://github.com/username',
            }),

            'linkedin_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://linkedin.com/in/username',
            }),
        }



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    full_name = forms.CharField(
        max_length=100,
        required=True
    )

    bio = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False
    )

    skills = forms.CharField(
        max_length=255,
        required=False
    )

    github_url = forms.URLField(required=False)

    linkedin_url = forms.URLField(required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'full_name',
            'bio',
            'skills',
            'github_url',
            'linkedin_url',
        ]