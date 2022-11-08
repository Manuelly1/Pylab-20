from django.shortcuts import render
from django.http import HttpResponse
from .models import Tecnologias
from django.shortcuts import redirect

def nova_empresa(request):
    if request.method == "GET":
        techs = Tecnologias.objects.all()
        return render(request, 'nova_empresa.html', {'techs': techs})
    elif request.method == "POST":
        nome = request.POST.get(('nome'))
        email = request.POST.get(('email'))
        cidade = request.POST.get(('cidade'))
        endereco = request.POST.get(('endereco'))
        nicho = request.POST.get(('nicho'))
        caracteristicas = request.POST.get(('caracteristicas'))
        tecnologias = request.POST.getList(('tecnologias'))
        logo = request.FILES.get('logo')


        if (len(nome.strip()) == 0 or len(email.strip()) == 0 or len(cidade.strip()) == 0 or len(endereco.strip()) == 0 or len(nicho.strip()) == 0 or len(caracteristicas.strip()) == 0 or (not logo)): 
            return redirect('/home/nova_empresa')

        if logo.size > 100_000_000:
            return redirect('/home/nova_empresa')

        if nicho not in [i[0] for i in Empresa.choices_nicho_mercado]:
            return redirect('/home/nova_empresa')

        return HttpResponse(tecnologias)
