from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from . import views 

urlpatterns = [
    path('', views.index, name='printers'),
    path('new/', views.new, name='new_printer'),
    path('<str:printer_id>/edit/', views.edit, name='edit_printer'),
    path('create', views.create, name='create_printer'),
    path('<int:printer_id>/', views.show, name='show_printer'),
    path('<int:printer_id>/update/', views.update, name='update_printer'),
    path('<int:printer_id>/destroy/', views.destroy, name='destroy_printer'),
]
