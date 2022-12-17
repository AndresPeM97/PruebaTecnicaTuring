from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from base.models import blog

def index(request):
    return render(request, "base/Inicio.html")

def nosotros(request):
    return render(request, "base/Nosotros.html")

def servicios(request):
    return render(request, "base/Servicios.html")

def tableau(request):
    return render(request, "base/Tableau.html")



def portalauth(request):
    return render(request, "base/PortalAuth.html")

class portal(LoginView):
    template_name = "base/Portal.html"
    field = "__all__"
    redirect_authenticated_user = True


    def get_success_url(self):
        return reverse_lazy("pagPortalAuth")

def blogs(request):

    articulos = blog.objects.all()

    return render(request, "base/Blog.html", {"articulos":articulos})

class DetalleBlog(DetailView):
    model = blog
    context_object_name = "articulo"
    template_name = "base/DetalleArticulo.html" #predeterimado es "tarea_detail"

def contacto(request):

    if(request.method=="POST"):
        subject = request.POST["asunto"]
        message = f"""{request.POST['nombre']} le ha enviado un correo de contacto

    {request.POST['mensaje']}
        
{request.POST['nombre']}
{request.POST['compania']}
{request.POST['email']}
{request.POST['telefono']}"""

        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["l18121591@morelia.tecnm.mx"]

        send_mail(subject, message, email_from, recipient_list)

    return render(request, "base/Contacto.html")

## servicios

def balanced(request):
    return render(request, "base/servicios/Balanced.html")

def bussines(request):
    return render(request, "base/servicios/Bussines.html")

def capacitacion(request):
    return render(request, "base/servicios/Capacitacion.html")

def dsoftware(request):
    return render(request, "base/servicios/Dsoftware.html")

def vhardware(request):
    return render(request, "base/servicios/Vhardware.html")

def vsoftware(request):
    return render(request, "base/servicios/Vsoftware.html")

def workshop(request):
    return render(request, "base/servicios/Workshop.html")

## tableau

def cloud(request):
    return render(request, "base/tableau/Cloud.html")

def desktop(request):
    return render(request, "base/tableau/Desktop.html")

def dmanage(request):
    return render(request, "base/tableau/Dmanage.html")

def prep(request):
    return render(request, "base/tableau/Prep.html")

def server(request):
    return render(request, "base/tableau/Server.html")

def smanage(request):
    return render(request, "base/tableau/Smanage.html")
