

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
    # Instala-se o Django, congela-se as bibliotecas, criar pp e pa
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

    urlpatterns = [
        path('', include('pa.urls'))
    ] 
    """

def pa():
    """"""
    # Dentro do pa, criam-se os diretórios: static & templates
    # Dentro do pa, criam-se os diretórios aninhados à static: css & images & js
    """
    pa/new/directory/static 
    pa/new/directory/css  pa/new/directory/images  pa/new/directory/js
    pa/new/directory/templates
    """

def views():
    """"""
    # Cria-se a view principal (tipo class based view)
    """
    from django.generic.views import TemplateView
    class IndexView(TemplateView)
        template_name = 'index.html'
    """

    # Cria-se a view principal (tipo function based view)
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
        path('', IndexView.as_view(), name='index'),  # class based view
        path('', index, name='index'),                # function based view
    ]
    """

def head():
    """"""
    # Posicionar antes de qualquer outra tag link
    """
    <link 
        crossorigin="anonymous"
        href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" 
        integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"
        rel="stylesheet">
    """

def body_script():
    """"""
    # Scripts mandatórios, sempre os últimos elementos da tag <body></body>
    """
    <script 
        crossorigin="anonymous"
        integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
        src="https://code.jquery.com/jquery-3.5.1.slim.min.js">
    </script>
    
    <script 
        crossorigin="anonymous"
        integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx"
        src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js">
    </script>
    """

def terminal2():
    """"""
    # Aplicar as migrações e iniciar o servidor
    """
    python manage.py migrate
    python manage.py runserver
    """
