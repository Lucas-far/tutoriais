

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 12:Adicionando outras funcionalidades
    Aula:   # 109. Trabalhando com paginação no Django
    """

def terminal():
    """
    pip install django
    pip install django-bootstrap4
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

def settings():
    """
    from os import path
    ALLOWED_HOSTS = ['*']
    INSTALLED_APPS = ['pa', 'bootstrap4']
    TEMPLATES = [{'DIRS': ['templates']}]
    """

def pp_urls():
    """
    from django.urls import include
    urlpatterns = [path('', include('pa.urls'))]
    """

# Observações
" Var || ordering    || ordena os itens de paginação pelo campo especificado no valor"
" Var || paginate_by || define a quantidade de elementos exibidos por página"
def views():
    """
    class IndexListView(ListView):
    model = Product
    ordering = 'description'
    paginate_by = 5           #
    template_name = 'index.html'
    """

def pa_urls():
    """
    from django.urls import path
    from .views import *

    urlpatterns = [
        path('', IndexListView.as_view(), name='index'),
    ]
    """

def models():
    """
    from django.db import models

    class Product(models.Model):
        name = models.CharField('Nome', max_length=150)
        price = models.DecimalField('Preço', decimal_places=2, max_digits=9)
        description = models.TextField('Sobre o produto')

        class Meta:
            verbose_name = 'Produto'
            verbose_name_plural = 'Produtos'

        def __str__(self):
            return self.name
    """

def admin():
    """
    from django.contrib import admin
    from .models import *

    @admin.register(Product)
    class ProductAdmin(admin.ModelAdmin):
        list_display = ('name', 'price', 'description')
    """

def terminal2():
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    """

def browser():
    """ 1. Acessar o template admin e criar 10 objetos """

# index.html (sintaxes estrangeiras pertencentes ao contexto de paginação)
"Classe  || page-item disabled    || retira a cor de um elemento de navagação (normalmente seta) não selecionado"
"Classe  || page-item active      || destaca a cor de um elemento de navagação (normalmente seta) selecionado"
"Método  || .has_next             || usado com a var (page_obj)"
"Método  || .has_previous         || usado com a var (page_obj)"
"Método  || .next_page_number     || usado com a var (page_obj)"
"Método  || .number               || usado com a var (page_obj)"
"Método  || .page_range           || usado com a var (paginator)"
"Método  || .previous_page_number || usado com a var (page_obj)"
"Sintaxe || &laquo;               || cria seta horizontal esquerda"
"Sintaxe || &raquo;               || cria seta horizontal direita"
"Var     || page_obj              ||"
"Var     || paginator             ||"
def templates():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página</title>
    </head>
    <body>
        <div class="container">
            <table class="table table-dark table-bordered border border-danger">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Nome</th>
                        <th>Preço</th>
                        <th>Descrição</th>
                    </tr>
                </thead>
                <tbody>
                {% for each_data in page_obj %}
                    <tr>
                        <td>{{ each_data.id }}</td>
                        <td>{{ each_data.name }}</td>
                        <td>{{ each_data.price }}</td>
                        <td>{{ each_data.description }}</td>
                    </tr>
                {% endfor %}
                </tbody>
                <tfoot></tfoot>
            </table>
            {% if is_paginated %}
                <nav aria-label="nav-page">
                    <ul class="pagination">
                    {% if page_obj.has_previous %}
                        <li class="page-item"><a class="page-link" href="?page={{ page_obj.previous_page_number }}">&laquo;</a></li>
                    {% else %}
                        <li class="page-item disabled"><a class="page-link" href="#">&laquo;</a></li>
                    {% endif %}

                    {% for each_page in paginator.page_range %}
                        {% if page_obj.number == each_page %}
                            <li class="page-item active"><a class="page-link" href="#">{{ each_page }}</a></li>
                        {% else %}
                            <li class="page-item"><a class="page-link" href="?page={{ each_page }}">{{ each_page }}</a></li>
                        {% endif %}
                    {% endfor %}

                    {% if page_obj.has_next %}
                        <li class="page-item"><a class="page-link" href="?page={{ page_obj.next_page_number }}">&raquo;</a></li>
                    {% else %}
                        <li class="page-item disabled"><a class="page-link" href="#">&raquo;</a></li>
                    {% endif %}
                    </ul>
                </nav>
            {% endif %}
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

# 1. A configuração de exibição dos elementos foi baseada na view (IndexListView)
def browser2():
    """ Testar a navegação dos elementos """

# A parte de paginação pode ser posta em outro template, para reduzir o tráfego de código em um template único
"pagination.html"
def templates2():
    """
    {% if is_paginated %}
        <nav aria-label="nav-page">
            <ul class="pagination">
            {% if page_obj.has_previous %}
                <li class="page-item"><a class="page-link" href="?page={{ page_obj.previous_page_number }}">&laquo;</a></li>
            {% else %}
                <li class="page-item disabled"><a class="page-link" href="#">&laquo;</a></li>
            {% endif %}

            {% for each_page in paginator.page_range %}
                {% if page_obj.number == each_page %}
                    <li class="page-item active"><a class="page-link" href="#">{{ each_page }}</a></li>
                {% else %}
                    <li class="page-item"><a class="page-link" href="?page={{ each_page }}">{{ each_page }}</a></li>
                {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
                <li class="page-item"><a class="page-link" href="?page={{ page_obj.next_page_number }}">&raquo;</a></li>
            {% else %}
                <li class="page-item disabled"><a class="page-link" href="#">&raquo;</a></li>
            {% endif %}
            </ul>
        </nav>
    {% endif %}
    """

# Para que o que foi explicado acima funciona, é preciso incluir o template dentro do outro
"Usar no escopo da tag <div></div> e fora do escopo da tag <table></table>"
def include():
    """ {% include 'pagination.html' %} """

def detalhes():
    """
    class IndexListView(ListView):
        ordering = '-id'     # mostra dados baseados em seus ids, em ordem decrescente
        ordering = '-name'   # mostra dados baseados em seus nomes (se foi criado), em ordem decrescente
        ordering = '-price'  # mostra dados baseados em seus preços (se foi criado), em ordem decrescente
    """