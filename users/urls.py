from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from .views import SessionView, RegistrationView, ProfileView
from . import views


urlpatterns = [
   path('accounts/', include('django.contrib.auth.urls')),
   path('sign_in', SessionView.as_view(), name = "sign_in"),
   path('sign_out', views.sign_out, name = "sign_out"),
   path('sign_up', RegistrationView.as_view(), name= "sign_up"),
   path('profile',ProfileView.as_view(), name = "profile"),
   path('', views.index, name='users'),
   path('new/', views.new, name='new_user'),
   path('<str:user_id>/edit/', views.edit, name='edit_user'),
   path('create', views.create, name='create_user'),
   path('<int:user_id>/', views.show, name='show_user'),
   path('<int:user_id>/update/', views.update, name='update_user'),
   path('<int:user_id>/destroy/', views.destroy, name='destroy_user'),
]  