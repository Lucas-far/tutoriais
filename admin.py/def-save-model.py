

def fonte():
    """
    Curso: Programação Web com Python e Django Framework: Essencial
    Aula: 66. Extendendo o Django User Model
    Tempo: a partir de 33:20
    """

def admin():
    """"""
    # Esqueleto
    """
    def save_model(self, request, obj, form, change):
       obj.field = request.user
       super().save_model(request, obj, form, change)
    """
