from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.session import SessionStore
from .models import User
from .forms import SignInForm, RegisterForm, UserForm
from django.urls import reverse

# Create your views here.
class SessionView(View):
    template_name = "sign_in.html"

    def get(self, request):
        context = { 'form': SignInForm()}
        print(request.session.get("_auth_user_id"))
        if request.session.get("_auth_user_id"):
            return redirect("/printers")

        return render(request, self.template_name, context)

    def post(self, request):
        form = SignInForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=email, password=password)
        if user is not None:
            s = SessionStore()
            s['_auth_user_id'] = user.id
            request.session["_auth_user_id"] = user.id
            s.save()
            s.create()
            return redirect("/")
        else:
            return render(request, "sign_in.html", {"form": form})


class RegistrationView(View):
    template_name = "register.html"

    def get(self, request):
        context = { 'form': RegisterForm()}
        if request.session.get("_auth_user_id"):
            return redirect("/printers")

        return render(request, self.template_name, context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.filter(email=form.cleaned_data["email"])
            return redirect("/printers")
        else:
            return render(request, "register.html", {"form": form})


def profile(request):
    user_id = request.session.get("_auth_user")
    if user_id:
        user = User.objects.get(pk=user_id)
        context = {"user": user}
        return render(request, "profile.html", context)
    else:
        print(SessionView.as_view())
        #return render(request, "sign_in.html", {"form": SignInForm})
        return HttpResponseRedirect('sign_in')

def index(req):
    users = User.objects.all()
    context = { 'users': users }
    return render(req, 'index.html', context)


def new(req):
    form = UserForm()
    user = req.POST
    return render(req, 'new.html', {'form': form})

def edit(req, user_id):
    user = User.objects.get(pk=user_id)
    form = UserForm(instance=user)
    return render(req, 'edit.html', {'form': form, 'id': user_id})

def show(req, user_id):
    user = User.objects.get(pk=user_id)
    context = { 'user': user }
    return render(req, 'user/show.html', context)

def create(req):
    form = UserForm(req.POST)
    if form.is_valid():
        form.save()
        return redirect('users')
    else:
        return render(req, 'new.html', {'form': form})

def update(req, user_id):
    user = User.objects.get(pk=user_id)
    form = UserForm(req.POST, instance=user)
    if form.is_valid():
        form.save()
        return redirect("/users")
    else:
        print(form.errors)
        return render(req, 'edit.html', {'form': form, 'id': user_id})

def destroy(req, user_id):
    for user in users:
        if user.id == user_id:
            users.remove(user)

    context = { 'users': users }
    return render(req, 'users/index.html', context)

def sign_out(req):
    print("cerrando sesion")
    if req.session.get("_auth_user_id"):
        req.session.flush()
        return redirect("home")

    return redirect("home")