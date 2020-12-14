

def views():
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
    """
    from .views import sign_in

    urlpatterns = [
        path('criar-conta', sign_in, name='criar-conta'),
    ]
    """

def head():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="{% static 'css/criar-conta.css' %}" rel="stylesheet">
        <meta charset="UTF-8">
        <title>Criar conta - tipo 2</title>
    </head>
    """

"Importante"
# No caso de tag formulário, a classe [ form-group ] ajuda na responsividade
# Então, não precisa-se usar a classe [ col ], mas é preciso usar [ ma = .ma{margin: auto;} ]
def body():
    """
    <body>

        <div class="container">
            <form action="{% url 'criar-conta' %}" method="post">
                {% csrf_token %}
                {% bootstrap_messages %}

                <div class="row">
                    <div class="col">
                        <button class="btn btn-dark"><a href="{% url 'index' %}">Voltar à página Inicial</a></button>
                    </div>
                </div>
                <div class="row">
                    <div class="ma mt">
                        <h1>Criação de conta</h1>
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
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """
