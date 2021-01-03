

# todo -> PARTE 1

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 11:Trabalhando com Geolocalização
    Aula:   # 96. Criando e configurando nosso projeto
    """

def terminal():
    """
    pip install django
    pip install geoip2
    pip install requests
    django-admin startproject pp .
    django-admin startapp pa
    pip freeze > requirements.txt
    """

def browser():
    """
    Pesquisa  # geolite2 city tar.gz
    Website   # https://github.com/DocSpring/geolite2-city-mirror

    1 - Criar uma conta para ter acesso aos downloads

        User   # erl********@out****.com
        Senha  # esw*************

    2. Clicar em [ download databases ] https://www.maxmind.com/en/accounts/443805/geoip/downloads

    3. Fazer o download:
                        GeoLite2 City
                        GeoLite2 Country
    """

# Procedimentos no OS, pós instalação
def os():
    """
    1 - Selecionar os módulos baixados: [ botão direito ] [ extract here ]

    Módulos baixados:
                     GeoLite2-City_20201110
                     GeoLite2-Country_20201110

    2 - Entrar nesses dois diretórios e copiar os módulos: [ GeoLite2-City.mmdb ] & [ GeoLite2-Country.mmdb ]
    3 - Voltar ao projeto
    4 - raiz / new / directory / geoip
    5 - Colar os módulos copiados em 2
    """

def browser2():
    """
    1 - Pesquisar por Yelp
    2 - Acessar o site
    3 - Criar uma conta
    4 - No rodapé da página, procurar pelo link [ Developers ] [ Yelp Fusion ] [ Get started ]
    5 - Preencher o formulário para criar uma nova aplicação
    6 - Confirma email
    7 - Pós confirmação, são exibidos: [ Client ID ] e [ API Key ]

         Client ID:
                   Vt655OilW8i12wu9pAQdqg
         API Key:
                 SujGnU5va3rahW0yqU5yTc1HraG7-qlRTK3lroBPuTbK6a0KZu
                 yLB7456TExcENAZ4gLBoT2qEzTCv3UKZa6J2jUZvywxzRvHVC9
                 DtxfwYBAP_5ECd-8ffE2S2OzX3Yx
    """

def settings():
    """
    INSTALLED_APPS = ['pa']
    TEMPLATES = [{'DIRS': ['templates']}]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    GEOIP_PATH = path.join(BASE_DIR, 'geoip')
    YELP_API_KEY = 'SujGnU5va3rahW0yqU5yTc1HraG7-qlRTK3lroBPuTbK6a0KZuyLB7456TExcENAZ4gLBoT2qEzTCv3UKZa6J2jUZvywxzRvHVC9DtxfwYBAP_5ECd-8ffE2S2OzX3Yx'
    """

# todo -> PARTE 2

def fonte2():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 11:Trabalhando com Geolocalização
    Aula:   # 97. Criando as rotas
    """

def pp_urls():
    """
    from django.urls import include
    urlpatterns = [path('', include('pa.urls'))]
    """

def pa_urls():
    """
    from django.urls import path
    from .views import IndexView
    urlpatterns = [path('', IndexView.as_view(), name='index')]
    """

# todo -> PARTE 3

def fonte3():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 11:Trabalhando com Geolocalização
    Aula:   # 98. Criando um utilitário para IPs e busca
    """

# Não existe, cria-se
def pa_utils():
    """
    import requests
    from random import randint
    from django.conf import settings
    from django.contrib.gis.geoip2 import GeoIP2
    from django.contrib.gis.geoip2 import geoip2

    YELP_SEARCH_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

    def yelp_search(keyword=None, location=None):
        headers = {"Authorization": "Bearer " + settings.YELP_API_KEY}

        if keyword and location:
            params = {'term': keyword, 'location': location}
        else:
            params = {'term': 'Restaurante', 'location': 'Teresina'}

        answer = requests.get(YELP_SEARCH_ENDPOINT, headers=headers, params=params)

        return answer.json()

    def get_data_client_site():
        site = GeoIP2()
        ip = get_random_ip()
        try:
            return site.city(ip)
        except geoip2.errors.AddressNotFoundError:
            return None

    def get_random_ip():
        return '.'.join([str(randint(0, 255)) for index_zero_to_three in range(4)])
    """

# todo -> PARTE 4

def fonte4():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 11:Trabalhando com Geolocalização
    Aula:   # 99. Criando a view
    """

def views():
    """
    from django.shortcuts import render
    from django.views.generic import View
    from .utils import get_data_client_site, yelp_search

    class IndexView(View):

        def get(self, request, *args, **kwargs):
            items = []
            city = None

            while not city:
                ret = get_data_client_site()
                if ret:
                    city = ret['city']

            loc = request.GET.get('loc' or None)
            q = request.GET.get('key' or None)
            location = city

            context = {'city': city, 'busca': False}

            if loc:
                location = loc
            if q:
                items = yelp_search(keyword=q, location=location)
                context = {'items': items, 'city': location, 'busca': True}

            return render(request, 'index.html', context)
    """

# todo -> PARTE 5

def fonte5():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 11:Trabalhando com Geolocalização
    Aula:   # 100. Criando os templates
    """

# Criação [ 01:45 até 09:45 ]
def templates_base():
    """
    <!DOCTYPE html>
    {% load static %}
    <html lang="en">
    <head>
        <link
            crossorigin="anonymous"
            href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
            integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"
            rel="stylesheet"
        >
        <link href="https://unpkg.com/leaflet@1.3.1/dist/leaflet.css" rel="stylesheet">
        <link href="{% static 'css/styles.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página Base</title>
        <style>
            .gmap {height: 400px; width: 100%;}
        </style>
    </head>
    <body>
        <div class="container text-center">
            {% block content %}{% endblock %}
        </div>

        <script
            crossorigin="anonymous"
            integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
            src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
        ></script>

        <script
            crossorigin="anonymous"
            integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx"
            src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js"
        ></script>

        <script src="https://unpkg.com/leaflet@1.3.1/dist/leaflet.js"></script>
    </body>
    </html>
    """

# Criação [ 13:40 até 27:07 ]
def templates_index():
    """
    {% extends 'base.html' %}
    {% block content %}
        <div class="row">
            <div class="col-sm-6">
                <form autocomplete="off" action="{% url 'index' %}">
                    {% csrf_token %}
                    <div class="form-group">
                        <h2><a href="{% url 'index' %}">Buscador</a></h2>
                        <h4>[{{ city }} {% if country %} - {{ country }} {% endif %}]</h4>
                    </div>
                    <div class="form-group">
                        <input class="form-control" type="text" name="key" placeholder="Pesquise sobre algo">
                        <small id="KeyHelp" class="form-text text-muted">Exemplo: academia, restaurante...</small>
                    </div>
                    <div class="form-group">
                        <input class="form-control" type="text" name="loc" placeholder="Pesquise uma cidade">
                        <small id="KeyLoc" class="form-text text-muted">Exemplo: França, Roraima...</small>
                    </div>
                    <button type="submit" class="btn btn-primary">Buscar</button>
                </form>
                {% if 'error' in items %}
                    <h2>Sem resultado para {{ city }}</h2>
                {% elif busca and items.businesses|length < 1 %}
                    <h2>Sem resultados</h2>
                {% elif city and items %}
                    <h2>Resultados</h2>
                    {% for biz in items.businesses %}
                        <span class="text-info">{{ biz.name }}, {{ city }}</span><br>
                    {% endfor %}
                {% endif %}
            </div>
            {% if city and items|length > 1 %}
                {% include 'maps.html' %}
            {% endif %}
    <!--    </div>-->
    {% endblock %}
    """

# Criação [ 27:10 até 39:55 ]
def templates_maps():
    """
    <div class="col-sm-6">
        <h2 class="text-secondary">Localidades</h2>
        <div class="gmap" id="mapDiv"></div>
    </div>
    </div>

    <script>
        var lat = {{ items.businesses.0.coordinates.latitude | safe }};
        var lon = {{ items.businesses.0.coordinates.longitude | safe }};
        var map = L.map('mapDiv').setView([lat, lon], 13);
        L.tileLayer(
            'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
             {attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors', maxZoom: 18,}
             ).addTo(map);

        {% for biz in items.businesses %}
            var = marker = L.marker(
                [{{ biz.coordinates.latitude | safe }}, {{ biz.coordinates.longitude | safe }}]
            ).addTo(map);

            marker.bindPopup(
                "<b>{{ biz.name }}</b><br>{{ biz.location.display_address.0 }}<br>{{ biz.location.display_address.1 }}<br>{{ biz.location.display_address.1 }}<br>{{ city }}").openPopup();
        {% endfor %}
    </script>
    <!--
    ========== Tradução de objetos em <script></script> ==========
    var = get_data_client_site() [ criado no módulo (utils.py) ]
    var = get_data_client_site() ------- var['businesses']
    13 = nível de zoom [ 0 a 18 ]
    -->
    """

# todo -> PARTE 6

def fonte6():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 11:Trabalhando com Geolocalização
    Aula:   # 100. Criando os templates
    """

def terminal2():
    """ python manage.py runserver """
