

def acesso():
    """"""

    # Primeiro, é preciso estar no django shell
    """ python manage.py shell """
def importar():
    """"""

    # Segundo, é preciso importar algo: seja variável, biblioteca, métodos, métodos aninhados, etc...
    # Exemplo: importando variável de módulo
    """
    from pp.settings import DEBUG
    dir(DEBUG)
    """

    # Exemplo: importando biblioteca
    """
    from django import forms
    dir(forms.Form)
    """

    # Exemplo: importando métodos
    """
    from django.db import models
    dir(Services.objects)
    """

    # Exemplo: importando métodos aninhados
    """
    from django.db import models
    dir(Services.objects.all)
    """
