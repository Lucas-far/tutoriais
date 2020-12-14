

def terminal():
    """"""

    """
    pip install bootstrap4
    pip freeze > requirements.txt
    """
def settings():
    """"""

    """
    INSTALLED_APPS = ['bootstrap4'] 
    STATIC_URL = '/static/'
    STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
    """
def views():
    """"""

    # É importante lembrar que, [ request.POST['string'] ] é o atributo [ name="" ] na tag <input>
    """
    from django.contrib.auth.models import User
    from django.contrib import messages
    
    def sign_in(request):

        if str(request.method) == 'POST':
            if str(request.POST['password']) == str(request.POST['password_confirm']):
                if User.objects.filter(username=request.POST['username']).exists():
                    messages.error(request, 'O nome de usuário já existe.')
                elif User.objects.filter(email=request.POST['email']).exists():
                    messages.error(request, 'Já há uma conta registrada com esse e-mail.')
                else:
                    new_user = User.objects.create_user(
                        first_name=request.POST['first_name'],
                        last_name=request.POST['last_name'],
                        username=request.POST['username'],
                        email=request.POST['email'],
                        password=request.POST['password']
                    )
                    new_user.save()
                    messages.success(request, 'Seu usuário foi cadastrado. Obrigado!')
            else:
                messages.error(request, 'Senha inicial e de confirmação, não são idênticas!')

        return render(request, 'criar-conta.html')
    """
def urls():
    """"""

    """
    from .views import sign_in

    urlpatterns = [
        path('criar-conta', sign_in, name='criar-conta'),
    ]
    """
def declarar():
    """"""

    """ 
    {% load bootstrap4 %} 
    {% load static %}
    """
def head():
    """"""

    # 1 - Não sei exatamente a utilidade, mas pe melhor ter no template
    # 2 - Primeira parte da instalação do Bootstrap
    # 3 - Vínculo HTML com CSS pessoal customizado em sintaxe Django
    """ 
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> 
    
    <link
        crossorigin="anonymous"
        href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
        integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"
        rel="stylesheet">
        
    <link href="{% static 'css/criar-conta.css' %}" rel="stylesheet">  <!-- Para django -->
    """
def body_scripts():
    """"""

    """
    <script
        crossorigin="anonymous"
        integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
        src="https://code.jquery.com/jquery-3.5.1.slim.min.js">
    </script>

    <script
        crossorigin="anonymous"
        integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx"
        src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js">
    </script>
    """
"Importante"
# No caso de tag formulário, a classe [ form-group ] ajuda na responsividade
# Então, não precisa-se usar a classe [ col ], mas é recomendável usar [ ma = .ma{margin: auto;} ]
def body():
    """"""

    # <form enctype="multipart/form-data"></form> para caso haja upload de imagem
    """
    <div class="container">
        <form action="#" method="post">

            <div class="row">
                <div class="col">
                    <button class="btn btn-dark"><a href="#">Voltar à página Inicial</a></button>
                </div>
            </div>
            <div class="row">
                <div class="ma mt">
                    <h1>Criação de conta</h1>
                    <hr>
                </div>
            </div>
            <div class="row mt">
                <div class="form-group ma mb">
                    <label for="first_name">Nome</label>
                    <input type="text" class="form-control" id="first_name" name="first_name">
                </div>
            </div>
            <div class="row">
                <div class="form-group ma mb">
                    <label for="last_name">Sobrenome</label>
                    <input type="text" class="form-control" id="last_name" name="last_name">
                </div>
            </div>
            <div class="row">
                <div class="form-group ma mb">
                    <label for="username">Nome de usuário/apelido</label>
                    <input type="text" class="form-control" id="username" name="username">
                </div>
            </div>
            <div class="row">
                <div class="form-group ma mb">
                    <label for="email">Seu e-mail</label>
                    <input type="email" class="form-control" id="email" name="email">
                </div>
            </div>
            <div class="row">
                <div class="form-group ma mb">
                    <label for="password">Senha</label>
                    <input type="password" class="form-control" id="password" name="password">
                </div>
            </div>
            <div class="row">
                <div class="form-group ma mb">
                    <label for="password_confirm">Confirmar senha</label>
                    <input type="password" class="form-control" id="password_confirm" name="password_confirm">
                </div>
            </div>
            <div class="row">
                <div class="ma mb">
                    <button class="btn btn-dark" type="submit">Registrar</button>
                </div>
            </div>

        </form>
    </div>
    """
def css():
    """"""

    """
    body {background-color: #171A21; color: #c7d5e0;}
    .btn-dark {margin-top: 20px;}
    .btn-dark:hover a {text-decoration: none;}
    hr {background-color: aqua; height: 3px; box-shadow: 0 0 50px aqua; border-radius: 10px; width: 100%;}
    .ma {margin: auto;}
    .mb {margin-bottom: 10px;}
    .mt {margin-top: 25px;}
    .mt2 {margin-top: 50px;}
    """
