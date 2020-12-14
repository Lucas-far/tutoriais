

def btn():
    """"""
    # Há algumas variações de classes parar botões
    """
    <button type="button" class="btn btn-primary">botão azul claro</button>
    <button type="button" class="btn btn-secondary">botão cinza escuro</button>
    <button type="button" class="btn btn-success">botão verde claro</button>
    <button type="button" class="btn btn-danger">botão salmão</button>
    <button type="button" class="btn btn-warning">botão amarelo queimado</button>
    <button type="button" class="btn btn-info">botão azul cião</button>
    <button type="button" class="btn btn-light">botão branco</button>
    <button type="button" class="btn btn-dark">botão preto fosco</button>
    <button type="button" class="btn btn-link">botão de link comum transparente</button>
    """

    # Se o seu botão for de formato apenas link (sem tag <button></button>), insira a classe: role="button"
    """ <a class="btn btn-primary" href="#" role="button">Link</a> """

def mb():
    """"""
    # Referente à propriedade:
    "{margin-bottom:;}"

    # Uso
    """ <tag class="mb-1 mb-2 mb-3 mb-4 mb-5 mb-6"></tag> """

def mt():
    """"""
    # Referente à propriedade:
    "{margin-top:;}"

    # Uso
    """ <tag class="mt-1 mt-2 mt-3 mt-4 mt-5 mt-6"></tag> """

def form_control():
    """ Classe para formatação de campo de formulário, normalmente inserido na tag <input> """
    # Exemplo
    """
    <form class="form-signin" id="this-form" method="post">
        {% csrf_token %}
        <label class="sr-only" for="username"></label>
        <input class="form-control mb-2" id="username" name="username" placeholder="e-mail" type="email" required>

        <label class="sr-only" for="password"></label>
        <input class="form-control" id="password" name="password" placeholder="senha" type="password" required>

        <button class="btn btn-block btn-lg btn-warning" form="this-form" type="submit">login/entrar</button>
        <p class="mt-2 text-muted">&copy; {% now 'Y' %}</p>
    </form>
    """

def form_signin():
    """ Layout de campos com tamanho pré-definido para formulários, normalmente formulários de login """
    # Exemplo
    """ <form class="form-signin"></form> """

def sr_only():
    """ Classe para esconder textos em tags textuais, tornando-os disponíveis somente para leitores de tela """
    # Exemplo
    """ <h2 class="sr-only">Eu estou escondido</h2> """

def text_right_text_left_text_center():
    """
    Classe para alinhamento de conteúdo, funcionando somente se a classe for inserida dentro de uma tag <div></div>
    """
    # Exemplo errado (não terá êxito em uma tag não <div></div>)
    """ <span class="container text-right">SPAN</span>"""

    # Exemplo certo
    """
    <div class="container text-center"><span>centro</span></div>
    <div class="container text-right"><span>direita</span></div>
    <div class="container text-left"><span>esquerda</span></div>
    """
