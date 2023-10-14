from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request,*args, **kwargs):
    # print(args)
    # print(kwargs)
    # print(request.user)
    return render(request, "home.html", {})

def contact_view(request,*args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request,*args, **kwargs):
    my_context = {
        "my_title": "About us",
        "my_age": 28,
        "my_last_name": "Lima",
        "my_list": [123, 233, "kelvin","Ana Beatriz", "Fabrício", 3435],
    } 

    return render(request, "about.html", my_context)

def imagem_view(request,*args, **kwargs):
    return render(request, "imagem.html", {})