from django.shortcuts import render
from galeria.models import Fotografia

    # 2:{"nome": "Gláxia NGC 1079",
    #    "legenda": "nasa.org / NASA / Hubble"},

def index(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request):
    return render(request, 'galeria/imagem.html')