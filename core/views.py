from django.shortcuts import render

# Create your views here.

def principal(request):
    return render (request, 'core/PaginaPrincipal.html')

def contacto(request):
    return render(request, 'core/Contacto.html')

def perifericos(request):
    return render(request, 'core/PaginaPerifericosDet.html')

def funkos(request):
    return render(request, 'core/PaginaFunkosDet.html')

def consolas(request):
    return render(request, 'core/PaginaConsolasDet.html')