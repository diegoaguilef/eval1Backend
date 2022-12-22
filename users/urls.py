from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from .views import SessionView, RegistrationView, profile


urlpatterns = [
   path('accounts/', include('django.contrib.auth.urls')),
   path('sign_in', SessionView.as_view(), name = "sign_in"),
   path('sign_out', SessionView.as_view(), name = "sign_out"),
   path('sign_up', RegistrationView.as_view(), name= "sign_up"),
   path('profile',profile, name = "profile"),

]  