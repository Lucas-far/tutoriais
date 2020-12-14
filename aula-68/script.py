

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 7:Dissecando o Django User Model
    Aula:   # 68. Login e Autenticação
    """

def template_base():
    """"""
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link id="bootstrap-css" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://getbootstrap.com/docs/4.0/examples/sign-in/signin.css" rel="stylesheet">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Sem título</title>
    </head>
    <body class="text-center">
        {% block content %}{% endblock %}
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    </body>
    </html>
    """

def template_index():
    """"""
    """
    {% extends 'base.html' %}
    {% block content %}
        <div class="container">
            {% if user.is_anonymous %}
                <h2 class="alert alert-dark">Você não está logado</h2>
                <h4>Gostaria de efetuar o login?</h4>
                <a class="btn btn-dark" href="{% url 'login' %}">sign in/entrar</a>
            {% else %}
                <div class="alert alert-primary mb-5 text-center" style="display: inline-block;"><span>Seja bem-vindo, {{ user.get_full_name }}.</span></div>
                <div><a class="btn btn-warning" href="{% url 'logout' %}">logout/sair</a></div>
            {% endif %}
        </div>
    {% endblock %}
    """

def template_login():
    """"""
    """
    {% extends 'base.html' %}
    {% block content %}
        <form class="form-signin" id="this-form" method="post">
            {% csrf_token %}
            <label class="sr-only" for="username">Campo para preencher email</label>
            <input class="form-control mb-2" id="username" name="username" placeholder="e-mail" type="email" required>
    
            <label class="sr-only" for="password">Campo para preencher senha</label>
            <input class="form-control" id="password" name="password" placeholder="senha" type="password" required>
    
            <button class="btn btn-block btn-lg btn-warning" form="this-form" type="submit">login/entrar</button>
            <p class="mt-2 text-muted">&copy; {% now 'Y' %}</p>
        </form>
    {% endblock %}   
    """
