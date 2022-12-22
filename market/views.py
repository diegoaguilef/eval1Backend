from django.shortcuts import render
from django.views import View
from printers.models import Printer, ShoppingCart
from users.models import User
from django.contrib.sessions.backends.db import SessionStore as DBStore
from django.contrib.sessions.base_session import AbstractBaseSession
from django.db import models
from django.views.generic.detail import DetailView

from users.session import SessionStore

# Create your views here.   
def index(req):
    user = User.objects.get(pk=req.session.get('_auth_user_id'))
    printers = Printer.objects.all()
    context= {'printers': printers, 'user': user}
    print(user.role)
    return render(req, 'home.html', context)

def whoweare(req):
    user = User.objects.get(pk=req.session.get('_auth_user_id'))
    context = {'user': user}
    return render(req, 'whoweare.html', context)

def add_to_cart(req, product_id, quantity):
    user = User.objects.get(pk=req.session.get('_auth_user_id'))

    shopping_cart = ShoppingCart(product_id=product_id, user_id=user.id, quantity=quantity)
    shopping_cart.save()
    shopping_carts = ShoppingCart.objects.get(user_id=user.id)
    return render(req, 'shopping_cart.html', {'shopping_carts': shopping_carts})

class ArticleDetailView(DetailView):

    model = Printer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ShoppingCartView(View):

    model = ShoppingCart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = 0
        for cart in context['shopping_carts']:
            total += cart.printer.price * cart.quantity

        context['total'] = total
        return context