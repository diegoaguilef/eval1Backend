from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from .views import VRegistro, sign_in, cerrar_session


urlpatterns = [
   path('accounts/', include('django.contrib.auth.urls')),
   path('registrar',VRegistro.as_view(), name = "registration"),
   path('login',sign_in, name = "login"),   
   path('logout',cerrar_session, name = "logout"),

]  