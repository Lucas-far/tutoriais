

def onde_achar():
    """
    python manage.py shell
    from pa.models import *
    dir(Modelo.objects)
    """

def onde_usar():
    """ No módulo [ views ] na var [ context ] para ordenar exibição de objetos de um bdd, aleatoriamente """

def como_usar():
    """ No parâmetro do método [ order_by() ], passa-se a string do nome de um campo, ou a string '?' """

def views():
    """
    def get_context_data(self, **kwargs):
        context = super(ModeloTemplateView, self).get_context_data(**kwargs)
        context['services'] = Services.objects.order_by('?').all()
        return context
    """
