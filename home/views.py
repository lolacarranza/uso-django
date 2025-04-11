from django.shortcuts import render
from django.http import HttpResponse

def inicio (request):
    return render (request, 'home/inicio.html')

def crear_auto (request):
    return render (request, 'home/crear_auto.html')

# Create your views here.