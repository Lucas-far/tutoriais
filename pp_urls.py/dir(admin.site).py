

def fonte():
    """
    Curso: Programação Web com Python e Django Framework: Essencial
    Aula: 66. Extendendo o Django User Model
    Tempo: a partir de 37:40
    """

def onde_achar():
    """
    python manage.py shell
    from django.contrib import admin
    dir(admin.site)
    """

def pp_urls():
    """"""
    # Procedimentos
    """
    from django.contrib import admin
    from django.contrib.auth.models import User
    
    admin.site.site_header = 'Python e Django'
    admin.site.site_title = f'Bem-vindo, admin {User.objects.get(username="Lucas").get_full_name()}'
    admin.site.index_title = 'Gerenciamento'
    """
    # Importação 1: mandatória
    # Importação 2: opcional
    # admin.site.site_header = Título da página de login do Django template admin
    # admin.site.site_title  = <title></title>
    # admin.site.index_title = <h1></h1> do menu do template admin Django

def obs():
    """"""
    # Em [ admin.site.site_title ] acima, não é necessário importação de algum bdd, isso foi apenas um floreio
    # Eu [ admin.site.site_title ] acima, poderia ser uma string qualquer
