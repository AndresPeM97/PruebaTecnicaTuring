from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.list import ListView

def index(request):
    return render(request, "base/Inicio.html")
