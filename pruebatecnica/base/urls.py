from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.index, name = "pagIndex"),
    path("Inicio/", views.index , name="pagInicio"),
    path("Nosotros/", views.nosotros, name = "pagNosotros"),
    path("Servicios/", views.servicios, name = "pagServicios"),
    path("Tableau/", views.tableau, name = "pagTableau"),
    path("Portal/", portal.as_view(), name = "pagPortal"),
    path("PortalLogOut/", LogoutView.as_view(next_page = "pagPortal"), name="pagPortalLogOut"),
    path("PortalAuth/", views.portalauth, name = "pagPortalAuth"),
    path("Blog/", views.blog, name = "pagBlog"),
    path("Contacto/", views.contacto, name = "pagContacto"),

    ## servicios

    path("Balanced/", views.balanced, name = "pagBalanced"),
    path("Bussines/", views.bussines, name = "pagBussines"),
    path("Capacitacion/", views.capacitacion, name = "pagCapacitacion"),
    path("Dsoftware/", views.dsoftware, name = "pagDsoftware"),
    path("Vhardware/", views.vhardware, name = "pagVhardware"),
    path("Vsoftware/", views.vsoftware, name = "pagVsoftware"),
    path("Workshop/", views.workshop, name = "pagWorkshop"),

    ##

    path("Cloud/", views.cloud, name = "pagCloud"),
    path("Desktop/", views.desktop, name = "pagDesktop"),
    path("Dmanage/", views.dmanage, name = "pagDmanage"),
    path("Prep/", views.prep, name = "pagPrep"),
    path("Server/", views.server, name = "pagServer"),
    path("Smanage/", views.smanage, name = "pagSmanage")


    
]
