

# Formas de extender o modelo User no módulo [ models ]
def forma1():
    """"""
    # A forma 1 acontece somente no módulo [ models ]
    """
    from django.db import models
    from django.contrib.auth.models import User
    
    class Post(models.Model):
        author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
        title = models.CharField('Título', max_length=100)
        text = models.TextField('Texto', max_length=400)
        
    def __str__(self):
        return self.title
    """

def forma2():
    """"""
    # A forma 2 precisa de mais configurações
    # Módulo [ settings ]
    """ AUTH_USER_MODEL = 'av.módulo' """

    # Módulo [ models ]
    """
    from django.db import models
    from django.conf import settings

    class Post(models.Model):
        author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Autor', on_delete=models.CASCADE)
        title = models.CharField('Título', max_length=100)
        text = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.title
    """

# De acordo com a aula 66 [ Extendendo o Django User Model ] essa forma é a mais usada
def forma3():
    """"""
    #
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
# Sobre a forma 3, ela continua no mesmo diretório [ User ], no módulo [ get_full_name() ]
