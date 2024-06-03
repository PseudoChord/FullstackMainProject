from django.urls import path

from . import views

from .views import update_user 

urlpatterns = [
    path('', views.home, name='home')   ,
    path('index', views.index, name='index')   ,
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),  # Add this line for logout
    path('create_user/',views.create_user),
    path('success/', views.success, name='success'),
    path('view_users/', views.view_users, name='view_users'),
    path('delete_user/<int:pk>/', views.UserDeleteViews.as_view(), name='delete_user'),
    path('update_user/<int:user_id>/', update_user, name='update_user'),


        
]