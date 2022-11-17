from django.urls import path
from . import views 

urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('', views.home, name='home'),
    path('whoweare', views.whoweare, name='whoweare'),
    path('<str:printer_id>/edit/', views.edit, name='edit'),
    path('create', views.create, name='create'),
    path('<int:printer_id>/', views.show, name='show'),
    path('<int:printer_id>/update/', views.update, name='update'),
    path('<int:printer_id>/destroy/', views.destroy, name='destroy'),

]