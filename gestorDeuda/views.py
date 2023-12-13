from django.shortcuts import render, redirect
from . import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from gestorDeuda.models import Deudas, DetallesDeuda
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def viewDeudas(request):
    if request.user.is_superuser:
        deudas = Deudas.objects.all()
        data = {'deudas': deudas}
        return render(request, 'gestorDeuda/tablaDeudasAdmin.html', data)
    if request.user.is_authenticated:
        deudas = Deudas.objects.filter(usuario=request.user)
        data = {'deudas': deudas}
        return render(request, 'gestorDeuda/tablaDeudas.html', data)

@login_required    
def agregar_deuda(request):
    if request.user.is_superuser:
        form_deuda = forms.Deuda()
        form_detalle_deuda = forms.DetalleDeuda()

        if request.method == 'POST':

            form_deuda = forms.Deuda(request.POST)
            form_detalle_deuda = forms.DetalleDeuda(request.POST)
        
            if form_deuda.is_valid() and form_detalle_deuda.is_valid():
                nueva_deuda = form_deuda.save(commit=False)
                nueva_deuda.usuario = request.user
                nueva_deuda.save()
                nuevo_detalle_deuda = form_detalle_deuda.save(commit=False)
                nuevo_detalle_deuda.deuda = nueva_deuda
                nuevo_detalle_deuda.save()
                finalizada = False
                return HttpResponseRedirect(reverse('formDeuda'))

        data = {
            'form_deuda': form_deuda,
            'form_detalle_deuda': form_detalle_deuda,
            'titulo': 'Insertar Deuda'
                }
        return render(request, 'gestorDeuda/formDeudaAdmin.html',data)

    if request.user.is_authenticated:
        form_deuda = forms.Deuda()
        form_detalle_deuda = forms.DetalleDeuda()

        if request.method == 'POST':

            form_deuda = forms.Deuda(request.POST)
            form_detalle_deuda = forms.DetalleDeuda(request.POST)
            
            if form_deuda.is_valid() and form_detalle_deuda.is_valid():
                nueva_deuda = form_deuda.save(commit=False)
                nueva_deuda.usuario = request.user
                nueva_deuda.save()
                nuevo_detalle_deuda = form_detalle_deuda.save(commit=False)
                nuevo_detalle_deuda.deuda = nueva_deuda
                nuevo_detalle_deuda.save()
                finalizada = False
                return HttpResponseRedirect(reverse('formDeuda'))

        data = {
            'form_deuda': form_deuda,
            'form_detalle_deuda': form_detalle_deuda,
            'titulo': 'Insertar Deuda'
                }
        return render(request, 'gestorDeuda/formDeuda.html',data)

    

def marcar_como_listo(request, detalle_id):
    detalle = DetallesDeuda.objects.get(pk=detalle_id)
    if detalle.cantidadCuota > 0:
        detalle.cantidadCuota -= 1
        detalle.save()
    return redirect('tablaDeudas')
    

@login_required
def editarDeuda(request, id):
    if request.user.is_superuser:
        deuda = Deudas.objects.get(id=id)
        deudaDetalle = DetallesDeuda.objects.get(id=id)
        form_deuda = forms.Deuda(instance=deuda)
        form_detalle_deuda = forms.DetalleDeuda(instance=deudaDetalle)
        if request.method == 'POST':
            form_deuda = forms.Deuda(request.POST, instance=deuda)
            form_detalle_deuda = forms.DetalleDeuda(request.POST, instance=deudaDetalle)
            if form_deuda.is_valid() and form_detalle_deuda.is_valid():
                print("Formulario valido")
                form_deuda.save()
                form_detalle_deuda.save()
                return HttpResponseRedirect(reverse('tablaDeudas'))
            else:
                print("Errores: ",form_deuda.errors)

        data = {'form_deuda': form_deuda,
                'form_detalle_deuda': form_detalle_deuda,
                'titulo':'Editar Deuda'
                }
        return render(request, 'gestorDeuda/formDeudaAdmin.html',data)

    if request.user.is_authenticated:
        deuda = Deudas.objects.get(id=id)
        deudaDetalle = DetallesDeuda.objects.get(id=id)
        form_deuda = forms.Deuda(instance=deuda)
        form_detalle_deuda = forms.DetalleDeuda(instance=deudaDetalle)
        if request.method == 'POST':
            form_deuda = forms.Deuda(request.POST, instance=deuda)
            form_detalle_deuda = forms.DetalleDeuda(request.POST, instance=deudaDetalle)

            if form_deuda.is_valid() and form_detalle_deuda.is_valid():

                print("Formulario valido")
                form_deuda.save()
                form_detalle_deuda.save()
                return HttpResponseRedirect(reverse('tablaDeudas'))
            else:
                print("Errores: ",form_deuda.errors)

        data = {'form_deuda': form_deuda,
                'form_detalle_deuda': form_detalle_deuda,
                'titulo':'Editar Deuda'
                }
        return render(request, 'gestorDeuda/formDeuda.html',data)

@login_required
def eliminarDeuda(request, id):
    if request.user.is_superuser:
        deuda = Deudas.objects.get(id = id)
        deuda.delete()
        return HttpResponseRedirect(reverse('tablaDeudas'))
        
    if request.user.is_authenticated:
        deuda = Deudas.objects.get(id = id)
        deuda.delete()
        return HttpResponseRedirect(reverse('tablaDeudas'))
        
    
@login_required
def viewPerfil(request):
    if request.user.is_superuser:
        return render(request, 'gestorDeuda/perfilAdmin.html')
    if request.user.is_authenticated:
        return render(request, 'gestorDeuda/perfil.html')

@login_required
def viewNotificaciones(request):
    if request.user.is_superuser:
        return render(request, 'gestorDeuda/notificacionesAdmin.html')
    if request.user.is_authenticated:
        return render(request, 'gestorDeuda/notificaciones.html')