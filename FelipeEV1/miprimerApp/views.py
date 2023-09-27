from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
    'nombre': 'Felipe',
    'apellido': 'Catalán',
    'profesion': 'Analista Programador',
    'edad': '19',
    'ciudad': 'Talca',
    'imagenmia': ''
    }
    return render(request, 'index.html' ,data)

def proyecto1(request):
    data = {
        'nombreproyecto': 'Reddit',
        'detalle': 'foro de temas libres',
        'cliente': 'Mundo entero',
        'anio': '2005',
        'imagenproyecto': 'https://cdn.siasat.com/wp-content/uploads/2023/06/reddit.jpg',
        'linkproyecto': 'https://www.reddit.com/'
    }
    return render(request, 'proyectos.html' ,data)

def proyecto2(request):
    data = {
        'nombreproyecto': 'TikTok',
        'detalle': 'aplicación de videos cortos',
        'cliente': 'Mundo entero',
        'anio': '2016',
        'imagenproyecto': 'https://play-lh.googleusercontent.com/BmUViDVOKNJe0GYJe22hsr7juFndRVbvr1fGmHGXqHfJjNAXjd26bfuGRQpVrpJ6YbA=w240-h480-rw',
        'linkproyecto': 'https://www.tiktok.com/es/'
    }
    return render(request, 'proyectos.html' ,data)

def proyecto3(request):
    data = {
        'nombreproyecto': 'RedHat',
        'detalle': 'distribución de sistema operativo',
        'cliente': 'Mundo entero',
        'anio': '1993',
        'imagenproyecto': 'https://yt3.googleusercontent.com/ytc/AOPolaTz73ONxrBITU_puYnWmw7E795FLfEqZoCBHbe9Mw=s900-c-k-c0x00ffffff-no-rj',
        'linkproyecto': 'https://www.redhat.com/es'
    }
    return render(request, 'proyectos.html' ,data)