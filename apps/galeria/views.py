from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages
from apps.galeria.forms import FotografiaForms

    # 2:{"nome": "Gláxia NGC 1079",
    #    "legenda": "nasa.org / NASA / Hubble"},

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Realize o login para acessar a página")
        return redirect ('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia" :fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Realize o login para acessar a página")
        return redirect ('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_buscado = request.GET['buscar']
        if nome_buscado:
            fotografias = fotografias.filter(nome__icontains=nome_buscado)
    
    return render(request, 'galeria/buscar.html', {"cards": fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect ('login')  
    
    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia cadastrada com sucesso!')
            return redirect('index')

    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request):
    pass

def excluir_imagem(request):
    pass