from django.shortcuts import render
from django.http import HttpResponse
from .models import Tecnologias

def nova_empresa(request):
    if request.method == "GET":
        techs = Tecnologias.objects.all()
        return render(request, 'nova_empresa.html', {'techs': techs})
    elif request.method == "POST":
        return HttpResponse("Tô aqui")