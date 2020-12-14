

def lembrete_importante():
    """"""

    """
    Os códigos que envolvem request, não podem ser consultados nem utilizados no Django Shell 
    Os códigos que envolvem request, são inseridos no módulo [ views.py ]
    Ao inserir os códigos no módulo [ views.py ], vá ao navegador e abra a rota da view
    O retorno do request é impresso no terminal da IDE
    """
def pa_views_exemplos_uso_request():
    """"""

    # Exemplos de códigos envolvendo: request
    """
    print(request)
    print(dir(request))
    print(dir(request.method))
    print(request.method)
    print(request.headers)

    for pk, each_object in enumerate(request.headers):
        print(pk, each_object)

    for pk, each_object in enumerate(request.headers.items()):
        print(pk, each_object)

    print(request.headers['User-Agent'])
    print(dir(request.user))
    print(request.user)
    print(request.user.first_name)  # Precisa ter sido preenchido
    print(request.user.last_name)   # Precisa ter sido preenchido
    print(request.user.email)
    print(request.user.last_login)
    print(request.user.password)
    """
def pa_views_exemplos_uso_request_customizado():
    """
    def test(request):

        print('1' * 100), print(request), print('1' * 100, '\n')
        print('2' * 100), print(dir(request)), print('2' * 100, '\n')
        print('3' * 100), print(dir(request.method)), print('3' * 100, '\n')
        print('4' * 100), print(request.method), print('4' * 100, '\n')
        print('5' * 100), print(request.headers), print('5' * 100, '\n')

        print('6' * 100)
        for pk, each_object in enumerate(request.headers):
            print(pk, each_object)
        print('6' * 100, '\n')

        print('7' * 100)
        for pk, each_object in enumerate(request.headers.items()):
            print(pk, each_object)
        print('7' * 100, '\n')

        print('8' * 100), print(request.headers['User-Agent']), print('8' * 100, '\n')
        print('9' * 100), print(dir(request.user)), print('9' * 100, '\n')
        print('10' * 50), print(request.user), print('10' * 50, '\n')
        print('11' * 50), print(request.user.first_name), print('11' * 50, '\n')  # Se preenchido
        print('12' * 50), print(request.user.last_name), print('12' * 50, '\n')   # Se preenchido
        print('13' * 50), print(request.user.email), print('13' * 50, '\n')
        print('14' * 50), print(request.user.last_login), print('14' * 50, '\n')
        print('15' * 50), print(request.user.password), print('15' * 50, '\n')
    """
