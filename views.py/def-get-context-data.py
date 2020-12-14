

def context_fbv():
    """
    from django.shortcuts import render

    def any_view(request):
        context = {'key': 'value'}
        return render(request, 'any_view.html')
    """

def context_cbv():
    """
    from django.views.generic import TemplateView
    from .models import Modelo, Modelo2

    class AnyView(TemplateView):
        def get_context_data(self):
            context = super(AnyView, self).get_context_data(**kwargs)
            key = 'value'
            context['key'] = key
            context['var'] = Modelo.objects.all()
            context['var2'] = Modelo2.objects.get(campo='valor').campo
            return context
    """
    # Tanto variáveis soltas, quanto objetos de modelos podem ser exibidos na função: get_context_data()

def template():
    """"""
    # function based view & class based views = mesma forma de chamada no template
    "<tag>{{ var dentro de [''] }}</tag>"
    # Exemplo contextual
    "<h1>{{ var }}</h1>"
