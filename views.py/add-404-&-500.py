

def terminal():
    """"""
    # 1. Instalar bootstrap4 não é obrigatório, mas é importante
    "pip install django-bootstrap4"

def settings():
    """"""
    # 1. Caso bootstrap4 não tenha sido instalado, ignorar a primeira variável
    # 2. Os templates para tratamento de erro são renderizados somente no modo produção (DEBUG = False)
    """
    INSTALLED_APPS = ['bootstrap4']
    DEBUG = False
    """

def urls():
    """"""
    # var = 'pacote aplicação.módulo.nome_template'
    # O nome dos templates, recomenda-se ser: 404.html e 500.html
    """ 
    handler404 = 'pa.views.404' 
    handler500 = 'pa.views.500'
    """

def views():
    """"""
    # O nome da view é opcional, mas minha preferência é por: handler400 & handler500
    """
    def handler404(request, exception):
        context = {'message': 'The requested page does not exist',}
        return render(request, '404.html', context)
        
    def handler500(request):
        context = {'message': 'The requested page does not exist',}
        return render(request, '500.html', context)
    """

def templates():
    """"""
    # Muda-se somente: <link href="{% static 'css/500.css' %}" rel="stylesheet">
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="{% static 'css/404.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <div>
            <h2 class="mb20px">{{ message }}</h2>
            <button class="btn btn-light">
                <a class="my-btn" href="{% url 'index' %}">Voltar à página inicial</a>
            </button>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

def css():
    """"""
    # Estilos
    """
    body {
        background-image: linear-gradient(to right, purple, mediumpurple); color: silver; font-family: verdana;
        margin: 20px;
    }
    .my-btn:hover {text-decoration: none;}
    .mb20px {margin-bottom: 20px;}
    """
