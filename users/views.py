from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User
from .forms import SignInForm, RegisterForm
from django.urls import reverse

# Create your views here.
class SessionView(View):
    template_name = "sign_in.html"

    def get(self, request):
        context = { 'form': SignInForm()}
        if request.session.get("_auth_user_id"):
            return redirect("/printers")

        return render(request, self.template_name, context)

    def post(self, request):
        form = SignInForm(request.POST)
        email = form.data.get("email")
        password = form.data.get("password")
        user = User.objects.get(email=email, password=password)
        if form.is_valid() and user is not None:
            request.session["_auth_user"] = user.id
            return redirect("/")
        else:
            print(form.errors)
            return render(request, "sign_in.html", {"form": form})

    def delete(self, request):
        if request.session.get("_auth_user"):
            request.session.pop("_auth_user")
            return redirect("/")


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
    context = { 'users': users }
    return render(req, 'users/index.html', context)

def home(req):
    context = { 'user': users }
    return render(req, 'home.html', context)


def new(req):
    form = UserForm()
    user = req.POST
    return render(req, 'users/new.html', {'form': form})

def edit(req, user_id):
    user = None
    for p in users:
        if str(p.id) == str(user_id):
            user = p

    form = UserForm(initial={
        'name': user.name})
    
    return render(req, 'users/edit.html', {'form': form, 'id': user_id})

def show(req, user_id):
    user = User.objects.get(pk=user_id)
    context = { 'user': user }
    return render(req, 'user/show.html', context)

def create(req):
    form = UserForm(req.POST)
    
    name = req.POST.get('name')
    created_at = req.POST.get('created_at')

    if form.is_valid():
        user = User(len(users) + 1, name, created_at)
        users.append(user)
        return render(req, 'users/show.html', {'form': form, 'user': user})
    else:
        return render(req, 'users/new.html', {'form': form})

def update(req, user_id):
    user = user.objects.get(pk=user_id)
    form = UserForm(req.POST, req.FILES, instance=user)
    if form.is_valid():
        form.save()
        return render(req, 'users/show.html', {'form': form, 'id': user_id, 'user': user})
    else:
        return render(req, 'users/edit.html', {'form': form, 'id': user_id})

def destroy(req, user_id):
    for user in users:
        if user.id == user_id:
            users.remove(user)

    context = { 'users': users }
    return render(req, 'users/index.html', context)