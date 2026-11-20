from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import ProfileForm, RegisterForm
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            Profile.objects.create(
                user=user,
                full_name=form.cleaned_data['full_name'],
                bio=form.cleaned_data['bio'],
                skills=form.cleaned_data['skills'],
                github_url=form.cleaned_data['github_url'],
                linkedin_url=form.cleaned_data['linkedin_url'],
            )

            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            next_url = request.GET.get('next')

            if next_url:
                return redirect(next_url)

            return redirect('home')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

@require_POST
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile.html', {
        'form': form,
        'profile': profile
    })

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('home')

    return render(request, 'accounts/delete_account.html')