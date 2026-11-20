from django import forms
from .models import Post, Project


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Share your coding journey, knowledge or ideas...',
                'rows': 4,
            })
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            'tech_stack',
            'github_url',
            'live_url',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Project title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your project...',
                'rows': 5,
            }),
            'tech_stack': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Python, Django, PostgreSQL...',
            }),
            'github_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://github.com/username/project',
            }),
            'live_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com',
            }),
        }