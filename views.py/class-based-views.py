

def mixin():
    """"""
    # Mixin é uma classe com métodos que tenham alguma funcionalidade para outras class based views
    # É recomendável que o seu nome sempre tenha o sufixo "Mixin" ao final, para melhorar sua identificação
    # Uma classe mixin sempre herda da palavra: object
    # Os métodos em uma classe mixin, viram herança, caso ela seja chamada em uma class based view
    # Por convenção, na execução da herança, as classes mixin são posicionados à esquerda do parâmetro

    # Exemplo básico de class based view
    """
    from django.views.generic import View
    class IndexView(View):
        def get(self, request):
            return render(request, 'index.html')
    """

    # Exemplo - criação de uma classe mixin
    """
    class MeuMixin(object):
        def metodo(self):
            ...
        def metodo2(self):
            ...
    """

    # Exemplo - Herança de uma class mixin numa class based view
    """
    class TemplateView(TemplateResponseMixin, ContextMixin, TemplateView):
        def get(self, request, *args, **kwargs):
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
    """

def base_generic_views():
    """"""
    """
    from django.views.generic import RedirectView
    from django.views.generic import TemplateView
    from django.views.generic import View
    """

def list_generic_view():
    """"""
    """ from django.views.generic.list import ListView """

def detail_generic_view():
    """"""
    """ from django.views.generic.detail import DetailView """

def edit_generic_view():
    """"""
    """
    from django.views.generic import CreateView
    from django.views.generic import DeleteView
    from django.views.generic import UpdateView
    from django.views.generic import FormView
    """

def view_def_vs_view_class():
    """"""
    # Exemplo básico de function based view
    """
    from django.shortcuts import render

    def index(request):
        return render(request, 'index.html')
    """

    # Exemplo básico de class based view
    """
    from django.views.generic import TemplateView

    def IndexTemplateView(TemplateView):
        template_name = 'index.html'
    """

def view_def_com_class():
    """"""
    # Exemplo de mesclagem entre function e class based view
    # A variável [ context ] está sendo usado no contexto: class based view
    # A variável [ context ] no contexto: class based view, fica dentro de uma função
    # A variável [ context ] nesse exemplo, não é a melhora forma.
    # Vá ao diretório [ class-based-views ] e leia o módulo [ context.py ]
    """
    from django.shortcuts import render
    from django.views.generic import TemplateView
    from .models import Modelo
    
    class IndexTemplateView(TemplateView):
        
        def get(self, request):
            context = {
                modelo_var = Modelo.objects.all()
            }
        return render(request, 'index.html', context)
    """
