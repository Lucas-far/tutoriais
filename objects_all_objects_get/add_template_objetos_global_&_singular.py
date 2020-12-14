

# todo -> PARTE 1

def views():
    """
    from .models import Modelo
    from django.shortcuts import render

    def people(request):
        var = Modelo.objects.all()
        return render(request, 'people.html')
    """

def pa_urls():
    """
    from django.urls import path
    from .views import *

    urlpatterns = [path('people', people, name='people')]
    """

def templates():
    """
    1. Pode-se criar uma tabel, com um loop for nela, que chama todos os objetos de um bdd
    2. O campo __str__ que é um texto, pode ser convertido em um link, que redireciona para outra rota customizada
    3. A intenção da conversão do campo __str__ para link, é fazer seus campos serem renderizados num template solo
    4. Portanto, são 2 templates:
    5. Template global     = carrega todos os objetos de um bdd
    6. Template individual = carrega cada campo do objeto individualmente
    """

def template_global():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="{% static 'css/users_table.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <div>
            <button class="btn btn-light withdraw-this-tag">
                <a class="button-with-a" href="{% url 'index' %}">Voltar para à página inicial</a>
            </button>
            <h2 class="withdraw-this-tag">Listagem de usuários</h2>
        </div>
        <div class="container">
            <table>
                <thead>
                    <tr>
                        <th>Nome completo</th>
                        <th>Gênero</th>
                        <th>E-mail</th>
                        <th>Nacionalidade</th>
                        <th>Idade</th>
                        <th>Nota pessoal</th>
                        <th>Passatempos</th>
                        <th>Descrição curta</th>
                    </tr>
                </thead>
                <tbody>
                {% for each_object in var %}
                    <tr>
                        <td><a class="td-with-a" href="{% url 'people' each_object.slug %}">{{ each_object.full_name }}</a></td>
                        <td>{{ each_object.gender }}</td>
                        <td>{{ each_object.email }}</td>
                        <td>{{ each_object.nationality }}</td>
                        <td>{{ each_object.age }}</td>
                        <td>{{ each_object.self_grade }}</td>
                        <td>{{ each_object.passtime }}</td>
                        <td>{{ each_object.brief_description }}</td>
                    </tr>
                {% endfor %}
                </tbody>
            </table>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

def template_global_css():
    """
    body {
        background-image: linear-gradient(to right, darkcyan, darkgoldenrod);
        color: silver;
        font-family: verdana;
        margin: 20px;
    }

    .button-with-a:hover {text-decoration: none;}

    .td-with-a {color: darkblue;}

    .td-with-a:hover {text-decoration: none;}

    th {
        border: silver solid 3px;
        color: black;
        padding: 5px;
        text-align: center;
    }

    .withdraw-this-tag {display: block; margin-bottom: 20px;}
    """

# todo -> PARTE 2

def views2():
    """
    from django.shortcuts import render
    from .models import People

    def person(request, slug):
        var = People.objects.get(slug=slug)

        context = {'var': var}

        return render(request, 'person.html', context)
    """
    # Configurando o template individual

def pa_urls2():
    """
    from django.urls import path
    from .views import *

    urlpatterns = [path('person/<str:slug>', people, name='people')]
    """

def template_individual():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="{% static 'css/single_user.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <div>
            <button class="btn btn-light withdraw-this-tag">
                <a class="button-with-a" href="{% url 'people' %}">Voltar</a>
            </button>
            <h2 class="withdraw-this-tag">Página individual do usuário</h2>
        </div>
        <div>
            <table>
                <thead>
                    <tr>
                        <th>Nome completo</th>
                        <th>Gênero</th>
                        <th>E-mail</th>
                        <th>Nacionalidade</th>
                        <th>Idade</th>
                        <th>Nota pessoal</th>
                        <th>Passatempos</th>
                        <th>Descrição curta</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{{ var.full_name }}</td>
                        <td>{{ var.gender }}</td>
                        <td>{{ var.email }}</td>
                        <td>{{ var.nationality }}</td>
                        <td>{{ var.age }}</td>
                        <td>{{ var.self_grade }}</td>
                        <td>{{ var.passtime }}</td>
                        <td>{{ var.brief_description }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

def template_individual_css():
    """
    body {
            background-image: linear-gradient(to right, crimson, dodgerblue);
            fonta-family: verdana;
            margin: 20px;
        }

        .button-with-a:hover {
            text-decoration: none;
        }

        table {
            background-image: linear-gradient(to right, dodgerblue, crimson);
        }

        table th {
            border: black solid 1px;
            padding: 7px;
            text-align: center;
        }

        table td {
            border: black solid 1px;
            padding: 7px;
            text-align: center;
        }

        .withdraw-this-tag {display: block; margin-bottom: 50px;}
    """
