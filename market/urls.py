
from django.urls import path
from . import views
from .views import ShoppingCartView, ArticleDetailView, SaleView, SalesView
urlpatterns = [
    path('', views.index, name='home'),
    path('whoweare', views.whoweare, name='whoweare'),
    path('product_detail/<int:pk>', ArticleDetailView.as_view(), name='product_detail'),
    path('shopping_cart/', ShoppingCartView.as_view(), name='shopping_cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('remove_cart_product/<int:cart_id>', views.remove_cart_product, name='remove_cart_product'),
    path('sale/<str:invoice_id>', SaleView.as_view(), name='sale'),
    path('buy', SaleView.as_view(), name='buy'),
    path('sales', SalesView.as_view(), name='sales'),
]
