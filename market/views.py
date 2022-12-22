from django.shortcuts import render
from django.views import View
from printers.models import Printer
from users.models import User
from django.contrib.sessions.backends.db import SessionStore as DBStore
from django.contrib.sessions.base_session import AbstractBaseSession
from django.db import models
from django.views.generic.detail import DetailView

class CustomSession(AbstractBaseSession):
    account_id = models.IntegerField(null=True, db_index=True)
    name = models.TextField(null=True)
    role = models.TextField(null=True)

    @classmethod
    def get_session_store_class(cls):
        return DBStore

class SessionStore(DBStore):
    @classmethod
    def get_model_class(cls):
        return CustomSession

    def create_model_instance(self, data):
        obj = super().create_model_instance(data)
        try:
            account_id = int(data.get('_auth_user'))
            print(data.items())
            print("Session")
        except (ValueError, TypeError):
            account_id = None
        obj.account_id = account_id
        if account_id is not None:
            user = User.objects.get(pk=account_id)
            obj.name = user.get_full_name()
            obj.role = user.get_role_name()
        return obj

# Create your views here.   
def index(req):
    printers = Printer.objects.all()
    context= {'printers': printers, 'role': req.session.get('role'), 'name': req.session.get('name'), 'account_id': req.session.get('account_id')}
    return render(req, 'index.html', context)

def whoweare(req):
    return render(req, 'whoweare.html')

class ArticleDetailView(DetailView):

    model = Printer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ShoppingCartView(View):

    model = Printer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context