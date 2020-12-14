

def pycharm():
    """"""
    # Primeiro, configura-se o novo ambiente virtual
    """
    1 - Abrir o software
    2 - New Project
    3 - Location: nome do projeto novo
    4 - New environment
    5 - Base interpreter 
    6 - Base interpreter   
    7 - Create
    """
    # 5 - Linux   = /usr/local/bin/python3.8
    # 6 - Windows = c:\users\nome do user\appdata\local\programs\python\python3.8\python.exe

def terminal():
    """"""

    # Instala-se o Django, congela-se as bibliotecas, cria-se um pp e um pa
    """
    pip install django
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

def settings():
    """"""
    # Registra-se o pa, configura-se o dirs
    """
    INSTALLED_APPS = ['pa']
    TEMPLATES = [{'DIRS': ['templates']}]
    """

def urls():
    """"""
    # Cria-se um redirecionamento de rota do pp urls, para o pa urls
    """
    from django.urls import include

    urlpatterns = [path('', include('pa.urls'))] 
    """

def pa():
    """"""
    # Dentro do pa, criar os diretórios: static (matriz) / css + images + js (aninhados static) / templates (matriz)
    """
    pa/new/directory/static 
    pa/new/directory/css  pa/new/directory/images  pa/new/directory/js
    pa/new/directory/templates
    """

def views():
    """"""
    # Cria-se a view principal (class based view)
    """
    from django.generic.views import TemplateView
    class IndexView(TemplateView)
        template_name = 'index.html'
    """

    # Cria-se a view principal (function based view)
    """
    from django.shortcuts import render
    def index(request):
        return render(request, 'index.html')
    """

def pa_urls():
    """"""
    # Configura-se o módulo [ urls.py ] do pa (o do pp já existe)
    """
    from django.urls import path
    from .views import *

    urlpatterns = [
        path('', IndexView.as_view(), name='index')   # exemplo class based view 
        path('', index, name='index')                 # exemplo function based view
    ]
    """

def declarar():
    """"""
    # Sintaxe Django para Bootstrap
    """
    {% load bootstrap4 %}
    {% load static %}
    """

def head():
    """"""
    # Carregar os módulos css do bootstrap
    """ {% bootstrap_css %} """

def body():
    """"""
    # Scripts mandatórios
    """ {% bootstrap_javascript jquery='full' %} """

def terminal2():
    """"""
    # Aplicar as migrações e iniciar o servidor
    """
    python manage.py migrate
    python manage.py runserver
    """
