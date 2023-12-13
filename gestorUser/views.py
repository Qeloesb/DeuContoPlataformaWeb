from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Usuario
from .forms import singUpForm
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

class LoginVista(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


def singUp(request):
    usuario = Usuario
    form = singUpForm
    if request.method == 'POST':
        form = singUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'gestorUser/singUp.html', {'form' : form })
    
def singUpAdmin(request):
    usuario = Usuario
    form = singUpForm
    if request.method == 'POST':
        form = singUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('singUpAdmin')
    return render(request, 'gestorUser/singUpAdmin.html', {'form' : form })    

def index(request):
    if request.user.is_superuser:
        return render(request, 'gestorUser/indexAdmin.html')
    elif request.user.is_authenticated:
        return render(request, 'gestorUser/indexUser.html')
    else:
        return render(request, 'index.html')

@login_required
def viewUsuarios(request):
    if request.user.is_superuser:
        usuarioLista = User.objects.all()
        data ={'usuarioLista': usuarioLista}
        return render(request, 'gestorUser/tablaUsuarios.html', data)