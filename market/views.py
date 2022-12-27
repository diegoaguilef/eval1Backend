from django.shortcuts import redirect, render
from django.views import View
from printers.models import Printer, Sale, ShoppingCart
from users.models import User
from django.contrib.sessions.backends.db import SessionStore as DBStore
from django.contrib.sessions.base_session import AbstractBaseSession
from django.db import models
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from users.session import SessionStore
import random


def gen_random_hex_string():
    return ''.join(random.choices('0123456789abcdef', k=10))

# Create your views here.   
def index(req):
    user = None
    if req.session.get('_auth_user_id'):
        user = User.objects.get(pk=req.session.get('_auth_user_id'))
    printers = Printer.objects.all()
    context= {'printers': printers, 'user': user}
    return render(req, 'home.html', context)

def whoweare(req):
    user = None
    if req.session.get('_auth_user_id'):
        user = User.objects.get(pk=req.session.get('_auth_user_id'))
    context = {'user': user}
    return render(req, 'whoweare.html', context)

def add_to_cart(req):
    user = None
    if req.session.get('_auth_user_id'):
        user = User.objects.get(pk=req.session.get('_auth_user_id'))
    else:
        return redirect('sign_in')
    quantity = req.GET.get('quantity')
    product_id = req.GET.get('product_id')
    shopping_cart = ShoppingCart(printer_id=product_id, user_id=user.id, quantity=quantity)
    shopping_cart.save()
    return redirect('shopping_cart')

def remove_cart_product(req, cart_id):
    user = None
    if req.session.get('_auth_user_id'):
        user = User.objects.get(pk=req.session.get('_auth_user_id'))
    shopping_cart = ShoppingCart.objects.get(pk=cart_id)
    shopping_cart.delete()
    return redirect('shopping_cart')

class SaleView(View):
    def get(self, request):
        user = None
        if request.session.get('_auth_user_id'):
            user = User.objects.get(pk=request.session.get('_auth_user_id'))
        else:
            return redirect('sign_in')

        invoice_id = request.GET.get('invoice_id')
        sales = Sale.objects.filter(invoice=invoice_id)
        context = {'sales': sales, 'user': user}
        return render(request,'sale.html', context)


    def post(self, request):
        user = None
        if request.session.get('_auth_user_id'):
            user = User.objects.get(pk=request.session.get('_auth_user_id'))
        else:
            return redirect('sign_in')
        shopping_cart_ids = request.POST.getlist('shopping_cart_ids')
        print(shopping_cart_ids)
        shopping_carts = ShoppingCart.objects.filter(id__in=shopping_cart_ids)
        invoice = gen_random_hex_string()
        for cart in shopping_carts:
            printer = Printer.objects.get(id=cart.printer.id)
            print(printer.name)
            printer.stock = printer.stock - cart.quantity
            printer.save()
            cart.enabled = False
            cart.save()
            s = Sale(invoice=invoice, user=user)
            s.save()
            s.shopping_carts.add(cart)

        sales = Sale.objects.filter(invoice=invoice)
        context = {'sales': sales, 'user': user}
        return render(request,'sale.html', context)



class ArticleDetailView(DetailView):

    model = Printer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = None
        if self.request.session.get('_auth_user_id'):
            user = User.objects.get(pk=self.request.session.get('_auth_user_id'))

        context['user'] = user
        return context


class ShoppingCartView(TemplateView):
    template_name ='shopping_cart.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = None
        if self.request.session.get('_auth_user_id'):
            user = User.objects.get(pk=self.request.session.get('_auth_user_id'))
        else:
            context['user'] = user
            return context
        total = 0
        shopping_carts = ShoppingCart.objects.filter(user_id=user.id, enabled=True)
        for cart in shopping_carts:
            total += cart.printer.price * cart.quantity

        context['total'] = total
        context['user'] = user
        context['shopping_carts'] = shopping_carts
        return context

class SalesView(TemplateView):
    template_name ='sales.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = None
        if self.request.session.get('_auth_user_id'):
            user = User.objects.get(pk=self.request.session.get('_auth_user_id'))
        else:
            context['user'] = user
            return context
        total = 0
        sales = Sale.objects.filter(user=user).distinct()
        context['sales'] = sales
        context['user'] = user
        return context