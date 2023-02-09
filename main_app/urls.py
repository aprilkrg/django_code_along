from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shows/', views.shows, name='shows'),
    path('shows/add/', views.show_create, name='show_create_form'),
    path('shows/<int:pk>/edit/', views.show_edit, name='show_edit_form'),
    path('shows/<int:pk>/delete/', views.show_delete, name='show_delete'),
    path('login/', views.login_page, name='login_page'),
    path('profile/', views.profile_show, name='profile')
]