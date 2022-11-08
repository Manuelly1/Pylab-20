from django.shortcuts import render
from django.http import HttpResponse

def nova_empresa(request):
    return render(request, 'nova_empresa.html')