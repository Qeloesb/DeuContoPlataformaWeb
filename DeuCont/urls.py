"""
URL configuration for DeuCont project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from gestorUser.views import *
from gestorDeuda.views import *
from gestorDeuCont.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('login/', LoginVista.as_view(template_name='gestorUser/login.html'), name='login'),
    path('singUp/', singUp, name='singUp'),
    path('singUpAdmin/', singUpAdmin, name='singUpAdmin'),
    path('tablaDeudas/', viewDeudas, name='tablaDeudas'),
    path('tablaUsuarios/', viewUsuarios, name='tablaUsuarios'),
    path('formDeuda/', agregar_deuda, name='formDeuda'),
    path('marcar_listo/<int:detalle_id>/', marcar_como_listo, name='marcar_como_listo'),
    path('deleteDeuda/<int:id>', eliminarDeuda, name='eliminarDeuda'),
    path('editarDeuda/<int:id>', editarDeuda, name='editarDeuda'),
    path('perfil/', viewPerfil, name='perfil' ),
    path('notificaciones/', viewNotificaciones, name='notificaciones'),
]
