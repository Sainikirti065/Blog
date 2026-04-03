from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('', views.post_list, name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('edit/<slug:slug>/', views.update_post, name='update_post'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
]