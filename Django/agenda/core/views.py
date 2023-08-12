from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http.response import Http404
from django.http.response import JsonResponse
from django.contrib import messages
from datetime import datetime
from datetime import timedelta
from .models import Evento


# Create your views here.

def get_evento(request, titulo_evento):
    db_evento = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse(db_evento)


def index(request):
    return redirect('/agenda/')


@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=1)
    eventos = Evento.objects.filter(usuario=usuario, data_evento__gt=data_atual)
    response = {'eventos': eventos}
    return render(request, 'agenda.html', response)


def login_user(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuario ou Senha Inválido")
    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}

    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        id_evento = request.POST.get('id_evento')
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        local = request.POST.get('local')
        usuario = request.user

        if id_evento:
            db_evento = Evento.objects.get(id=id_evento)

            if usuario == db_evento.usuario:
                db_evento.titulo = titulo
                db_evento.descricao = descricao
                db_evento.data_evento = data_evento
                db_evento.local = local
                db_evento.save()
        else:
            Evento.objects.create(
                titulo=titulo,
                data_evento=data_evento,
                descricao=descricao,
                usuario=usuario,
                local=local
            )
    return redirect('/')


@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        db_evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()

    if usuario == db_evento.usuario:
        db_evento.delete()
    else:
        raise Http404
    return redirect('/')


@login_required(login_url='/login/')
def json_lista_evento(request):
    usuario = request.user
    db_evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo', 'data_evento', 'local', 'usuario')
    return JsonResponse(list(db_evento), safe=False)


@login_required(login_url='/login/')
def lista_historico(request):
    usuario = request.user
    data_atual = datetime.now()
    db_evento = Evento.objects.filter(usuario=usuario, data_evento__lt=data_atual)
    response = {'eventos': db_evento}
    return render(request, 'historico.html', response)
