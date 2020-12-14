

def para_entender_leia_isto():
    """"""
    # Um bdd é criado: [ Post ]
    # Um dos campos do bdd recebe dois métodos: [ models.ForeignKey ] [ get_user_model() ]
    # O método [ models.ForeignKey ] cria campos de escolha de algum bdd
    # O bdd escolhido é [ User ], indiretamente, pelo método [ get_user_model() ]
    # O def __str__ do bdd [ User ] é [ self.username ]
    # Os campos mostrados pelo [ models.ForeignKey ] = campo [ username ] do bdd [ User ]
    # Mas isso pode ser modificado no módulo [ admin ]
    # Pega-se o campo que recebe [ models.ForeignKey ] & [ get_user_model() ], ou seja: [ author ]
    # Edita-se esse campo na var list_display com a adição de um: _
    # O campo [ author ], torna-se: [ _author ]
    # Cria-se uma função com o nome do campo editado: [ _author ]
    # Retorna-se o campo que deseja-se ver
    # No contexto deste exemplo, o campo escolhido para ser visto, foi: [ first_name + last_name ]
    # [ first_name + last_name ] é a mesclagem que o método [ get_full_name() ] executa
    # Obviamente, se não foi dado valor para: [ first_name & last_name ], então [ get_full_name() ] será inútil
    # Poderia ser qualquer outro campo, por exemplo: [ pk ] [ first_name ] [ email ]
    # Mesmo vendo o campo [ username ] na hora de criar um objeto no template...
    # Quando for clicado em [ salvar ] o que é mostrado no campo [ author ], será: [ author.get_full_name() ]

def models():
    """"""
    """
    from django.db import models
    from django.contrib.auth import get_user_model
    
    class Post(models.Model):
        author = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)
        title = models.CharField('Título', max_length=100)
        text = models.TextField('Texto', max_length=400)
    
        def __str__(self):
            return self.title
    """

def admin():
    """"""
    """
    from django.contrib import admin
    from .models import *
    
    @admin.register(Post)
    class PostAdmin(admin.ModelAdmin):
        list_display = ('_author', 'title')
    
        def _author(self, instance):
            return f'{instance.author.get_full_name()}'
    """
    # Outros exemplos
    # return f'{instance.author.pk}'
    # return f'{instance.author.email}'
