from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows, name='shows'),
    path('add/', views.show_create, name='show_create_form'),
    path('<int:pk>/edit/', views.show_edit, name='show_edit_form'),
    path('<int:pk>/delete', views.show_delete, name='show_delete'),
    path('login/', views.login_page, name='login_page'),
    path('profile/', views.profile_show, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.register, name='signup_form'),
]