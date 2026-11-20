from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('community/', views.community, name='community'),
    path('projects/', views.projects, name='projects'),
    path('create/', views.create_post, name='create_post'),
    path('<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('projects/create/', views.create_project, name='create_project'),
    path('projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'),
]