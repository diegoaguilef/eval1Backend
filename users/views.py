from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.
class VRegistro(View):
    
    def get(self, request):
        if request.session.get("_auth_user_id"):
            return redirect('/printers')
        else:
            return render(request,'register.html', {'form': UserCreationForm})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            
            return redirect('/printers')
        
        else:
            for msg in form.error_messages:
                 messages.error(request, form.error_messages[msg])
            
            return render(request,'register.html', {'form': form})

def cerrar_session(request):
    logout(request)
    return redirect('login')

def sign_in(request):
    if request.session.get("_auth_user_id"):
        return redirect('/printers')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                nombre_usuario = form.cleaned_data.get("username")
                contraseña = form.cleaned_data.get("password")
                usuario = authenticate(request, username = nombre_usuario, password = contraseña)
                if usuario is not None:
                    login(request, usuario)
                    return redirect('/printers')
                else:
                    messages.error(request, messages,"Usuario inexistente")
            else:
                messages.error(request, messages,"Informacion incorrecta")
        return render(request,'registration/login.html', {'form': AuthenticationForm})



            


