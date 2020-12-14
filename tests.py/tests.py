

def fonte():
    """
    Curso:        # Programação Web com Python e Django framework: Essencial
    Aula pausada: # 59. Entendendo e configurando os testes
    Minuto:       # 08:27
    """

def teste_normal():
    """"""
    # Exemplo de teste que não envolve os módulos internos
    # Após escrever o teste, o comando abaixo deve ser executado no terminal
    # python manage.py test
    """
    from django.test import TestCase

    def remover_vogais(string):
        container = []
        vowels = ['a', 'e', 'i', 'o', 'u',
                  'à', 'á', 'â', 'ã',
                  'é',
                  'í',
                  'ó', 'ô', 'õ', 'ò'
                  'ú',
                  ]
        for lt in string:
            container.append(lt)
        for lt in vowels:
            while lt in container:
                container.pop(container.index(lt))
        container = ''.join(container)
        return container

    class FirstTestCase(TestCase):
        def setUp(self):
            self.texto = 'Lucas Farias Santos de Sousa'

        def test_remover_vogais(self):
            frase = remover_vogais(self.texto)
            self.assertTrue(frase == 'Lcs Frs Snts d Ss')
    """

# O teste normal é mais incomum de ser usado, sendo assim, há outras opções, uma delas vêm abaixo

def obs():
    """"""
    # O Django vêm com um módulo [ tests.py ] dentro do pacote aplicação
    # Mas como há testes variados, é melhor que delete-se esse módulo, e crie-se, ao invés, um diretório [ tests ]
    # O diretório [ tests ] também é criado no pacote aplicação
    # O que deve-se fazer a seguir:
    """
    pa/new/python file/__init__
    pa/new/python file/test_forms
    pa/new/python file/test_models
    pa/new/python file/test_views
    """

def instalar_pacotes_extra():
    """"""
    # Auxiliadores para melhoria dos testes
    """ 
    pip install model_mommy coverage
    pip freeze > requirements.txt
    """

def pacote_coverage_configurar():
    """"""
    # O pacote precisa receber um módulo com configurações específicas
    """ raiz/new/file/.coveragerc (módulo txt) """

    # Dentro do módulo txt criado:
    """ 
    [run]
    source = .

    omit = 
        */__init__.py
        */settings.py
        */manage.py
        */wsgi.py
        */apps.py
        */urls.py
        */admin.py
        */migrations/*
        */tests/*
    """

def projeto_em_html():
    """"""
    # Esse procedimento transfere seu projeto, inclusive os testes, para serem vistos em html, ao invés de terminal
    # Isso acontece por meio de comandos coverage, e posteriormente, acesso à um servidor local

    # .gitignore (se há deploy)
    # OBJETIVO: ignorar diretório [ htmlcov ], quando/se criado:
    """ htmlcov/* """

    # Esses dois códigos são práticos, mas há um problema
    # Eles não mostram o que testar, e pra isso é preciso usar os códigos que vem abaixo
    #------------------------------------------------------------------------------------------------------------------
    # Terminal
    # OBJETIVO: Executar teste após sua criação
    """ coverage run manage.py test """

    # Terminal
    # OBJETIVO: Retornar o progresso dos testes
    """ coverage report """
    #------------------------------------------------------------------------------------------------------------------
    # Terminal (não obrigatório)
    # OBJETIVO: deletar diretório [ htmlcov ] criado pelo comando [ html coverage ]
    """ rm -rf htmlcov """

    # Terminal
    # OBJETIVO: criar versão html do seu projeto python django por outro servidor local
    """ coverage html """

    # Terminal
    # OBJETIVO: Rodar o servidor local, se o comando [ coverage html ] tiver sido executado
    """ python -m http.server """
