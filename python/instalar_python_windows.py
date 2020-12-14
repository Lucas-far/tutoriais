

# Em caso de falhas nos comandos de terminal, pós a instalação do Python
def alertas():
    """
    PROCEDIMENTOS PESSOAIS:
        1. Desinstalar o Python e seu launcher [ C:\Users\meu_user\AppData\Local\Programs\Python ]
        2. Talvez instalar uma variável de ambiente para usuário, antes de instalar o Python
    """

# Softwares: 1. Java development kit (oracle) / 2. Python / 3. Pycharm
def softwares():
    """
    1. 04-jdk-11.0.7_linux-x64_bin.tar.gz
       FONTES:
             Google = Java Archive Downloads - Java SE 11 - Oracle
             https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html

    2. python-3.8.5.tar.xz
       FONTES:
              https://www.python.org/downloads/
              Site / Downloads / All releases

    3. pycharm-community-2020.2.tar.gz
    4. CONTA ORACLE: [ lu******2@g****.com ] [ W******s17 ]
    """

# Verificar se o Java encontra-se no OS
def terminal():
    """ java --version """

def configurar_java():
    """
    1. Após baixar o executável do Java, ele é normalmente instalado em: [ C:\Program Files\Java\jdk-11.0.7 ]
    2. Acessar [ C:\Program Files\Java\jdk-11.0.7\bin ] (ctrl + c)
    3. Ir ao local especificado em 4
    4. Este computador / propriedades / opções avançados do sistema / variáveis de ambiente / path / editar / novo
    5. [ C:\Program Files\Java\jdk-11.0.7\bin ] (ctrl + v)

       OBSERVAÇÕES:
                   1. No Windows 10, cada rota é criada em uma linha separada
                   2. Em outras versões do Windows, só há uma linha para todas as rotas
                      Portanto, em versões mais antigas, adiciona-se [ ; ] ao início e final da criação da rota binária
    """

# Verificar se o Java encontra-se no OS
def terminal2():
    """ java --version """

def configurar_python_parte1():
    """
    1. Abrir o executável
    2. Marcar [ Launcher ] & [ add python to PATH ] e continuar a instalação normalmente
    """

# Testar se a instalação do Python teve êxito
def terminal3():
    """
    [ python --version                              ] para verificar retorno de versão
    [ (python -m) pip --version                     ] para verificar existência do pacote pip python
    [ (python -m) pip install --upgrade pip         ] para atualizar o pacote pip python
    [ (python -m) pip install virtualenv            ] para habilitar criação de ambientes virtuais
    [ (python -m) pip install virtualenvwrapper-win ] para habilitar criação de ambientes virtuais isolados
    """

def configurar_python_parte2():
    """
    1. Ir ao local especificado abaixo:
    2. Este computador / propriedades / opções avançados do sistema / variáveis de ambiente / variáveis de usuário / novo

       INSTALAÇÃO DA VARIÁVEL DE AMBIENTE:
                                          Nome: WORKON_HOME
                                          Rota: C:\Users\meu_user\pasta_criada_para_armazenar_ambientes
    """

# Verificar se a variável de ambiente foi criada
def terminal4():
    """ echo %WORKON_HOME% """

# Com o virtualenv instalado, é preciso conhecer alguns comandos essenciais
def terminal5():
    """
    mkvirtualenv nome do av   # criação e login em um av
    deactivate                # deslogar de um av criado
    work on nome do av        # relogar em um av criado
    rmvirtualenv nome do av   # remover um av especificado
    """

def configurar_pycharm():
    """
    1. Abrir o executável e instalar
    2. Marcar [ create shortcut 64 bit ] [ create associations .py ]
    3. New Project
    4. Há duas formas de criar um projeto novo

    FORMA 1:
            Quando um ambiente não foi criado usando o comando mkvirtualenv

    1. Tela de entrada           = [ Location ] = inserir o nome do av
    2. Tela de entrada           = [ new environment ] = [ Base Interpreter ] = [ ... ]
    3. Select python interpreter = [ C:\users\meu_user\appdata\local\programs\python\python38\python.exe ]

    FORMA 2:
            Quando um ambiente já foi criado usando o comando: [ mkvirtualenv ]

    1. Tela de entrada           = [ Location ] = inserir o nome do av
    2. Tela de entrada           = [ Existing Interpreter ] = [ ... ]
    3. Add Python Interpreter    =

       EXEMPLO DE SINTAXE:
           [ C:\users\meu_user\pasta_criada_para_armazenar_ambientes\pasta_do_ambiente\scripts\python.exe ]
       EXEMPLO PRÁTICO:
           [ C:\users\lucas\Envs\ambiente\scripts\python.exe ]
    """
