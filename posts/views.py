
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Post, Project
from .forms import PostForm, ProjectForm
from accounts.models import Profile
from django.db import models



# Home Page
def home(request):
    context = {
        'message': 'Connect with developers, share ideas, and grow together!'
    }
    return render(request, 'home.html', context)


# Display All Posts
@login_required
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'posts/post_list.html', {
        'posts': posts
    })


# Community Page
@login_required
def community(request):
    profiles = Profile.objects.select_related('user').order_by(
    models.Case(
        models.When(user=request.user, then=0),
        default=1,
        output_field=models.IntegerField(),
    ),
    'user__username'
)
    return render(request, 'community.html', {
        'profiles': profiles
    })


# Projects Page
@login_required
def projects(request):
    projects = Project.objects.all().order_by('-created_at')

    return render(request, 'projects.html', {
        'projects': projects
    })


# Create Post
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('post_list')

    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', {
        'form': form
    })


# Edit Own Post
@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        return HttpResponseForbidden(
            "You cannot edit this post."
        )

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('post_list')

    else:
        form = PostForm(instance=post)

    return render(request, 'posts/edit_post.html', {
        'form': form
    })


# Delete Own Post
@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        return HttpResponseForbidden(
            "You cannot delete this post."
        )

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, 'posts/delete_post.html', {
        'post': post
    })


@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('projects')
    else:
        form = ProjectForm()

    return render(request, 'projects/create_project.html', {
        'form': form
    })

@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if project.owner != request.user:
        return HttpResponseForbidden("You cannot edit this project.")

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'projects/edit_project.html', {
        'form': form,
        'project': project,
    })

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if project.owner != request.user:
        return HttpResponseForbidden("You cannot delete this project.")

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    return render(request, 'projects/delete_project.html', {
        'project': project
    })