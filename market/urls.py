
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('whoweare', views.whoweare, name='whoweare'),
    path('product_detail/<int:pk>', views.ArticleDetailView.as_view(), name='product_detail'),
    path('shoppiong_cart/', views.ShoppingCartView.as_view(), name='shoppiong_cart'),
]
