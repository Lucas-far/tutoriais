

def models():
    """"""
    # Modelo base é um modelo com campos genéricos, criados para serem herdados por bdds principais
    # Classe Meta aninhada é obrigatória, para que esse modelo seja descartado de registro no módulo [ admin ]
    """
    from django.db import models

    class Base(models.Model):
        creation = models.DateTimeField('Data de criação', auto_now_add=True)
        updated = models.DateTimeField('Última atualização', auto_now=True)
        availability = models.BooleanField('Disponível', default=True)

        class Meta:
            abstract = True
    """
