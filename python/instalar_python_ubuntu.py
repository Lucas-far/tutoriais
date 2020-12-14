

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

def configurar_java():
    """
    1. O módulo normalmente vai para o diretório do Downloads do OS. No Ubuntu: /home/meu_user/Downloads
    2. Extrai o módulo [ .tag.gz ] no mesmo local onde ele está
    3. Renomear o diretório para [ jdk11 ]
    4. Se há módulos aninhados, leve todos para o diretório matriz
    5. /home/meu_user/apps (se não existe, criar)
    6. Retornar para /home/meu_user
    7. ctrl + h (mostrar módulos ocultos)
    8. Procurar e abrir [ .bashrc ]
    9. Vá ao final do módulo e adicione as seguintes linhas de código:

        JAVA_HOME=/home/meu_user/apps/jdk11
        export JAVA_HOME
        PATH=$PATH:$JAVA_HOME/bin
        export PATH

    10. Ir ao terminal, e checar se o Java foi instalado: [ java --version ]
    11. Se há um retorno da versão do Java, então teve sucesso
    """

# Atualizam-se os pacotes do Ubuntu
def terminal():
    """ sudo apt-get update """

# É recomendável outras ferramentas essenciais
def terminal2():
    """
    sudo apt install build-essential curl libbz2-dev libffi-dev libgdbm-dev libjpeg-dev liblzma-dev libncurses5-dev
    libnss3-dev libreadline-dev libsqlite3-dev libssl-dev sqlite3 zlib1g-dev
    """

def configurar_python():
    """
    1. O módulo normalmente vai para o diretório do Downloads do OS. No Ubuntu: /home/meu_user/Downloads
    2. Extrai o módulo [ .tag.gz ] no mesmo local onde ele está
    3. Entrar na pasta extraida do Python
    4. open in terminal

       TERMINAL:
                1. ./configure --enable-optimizations --with-ensurepip=install
                2. make -j 2
                3. sudo make altinstall
                4. python 3 --version / python3.8 --version
                5. pip3.8 --version
                6. sudo pip3.8 install --upgrade pip
                7. sudo pip3.8 install virtualenv virtualenvwrapper

    5. Retornar para /home/meu_user
    6. ctrl + h (mostrar módulos ocultos)
    7. Procurar e abrir [ .bashrc ]
    8. Vá ao final do módulo e adicione as seguintes linhas de código:

       export WORKON_HOME=$HOME/.virtualenvs
       export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.8  # terminal: which python3.8
       source /usr/local/bin/virtualenvwrapper.sh
    """

# Com o virtualenv instalado, é preciso conhecer alguns comandos essenciais
def terminal3():
    """
    mkvirtualenv nome do av   # criação e login em um av
    deactivate                # deslogar de um av criado
    work on nome do av        # relogar em um av criado
    rmvirtualenv nome do av   # remover um av especificado
    """

def configurar_pycharm():
    """
    1. O módulo normalmente vai para o diretório do Downloads do OS. No Ubuntu: /home/meu_user/Downloads
    2. Extrai o módulo [ .tag.gz ] no mesmo local onde ele está
    3. Renomear o diretório para [ pycharm ]
    4. Recortar (ctrl + x) o diretório [ pycharm ] para a rota: [ /home/meu_user/apps/ ]
    5. Entrar no diretório [ pycharm ]
    6. Entrar no diretório aninhado [ bin ]
    7. open in terminal
    8. sudo apt-get install alacarte -y

    CRIAR UM ÍCONE PARA O SOFTWARE PYCHARM

    1. Ir ao Desktop, em [ Show applications ]
    2. Procurar e abrir [ Main Menu ]
    3. [ Applications ] = [ Programming ]
    4. [ New item ] [ Name: Pycharm ] [ Command: /home/apps/pycharm/bin/pycharm.sh ]
    5. Adicionar um ícone: [ /home/lucas/apps/pycharm/bin/pycharm.png ]
    """

# Configuração essencial para criar projetos no Pycharm
def pycharm():
    """
    1. Abrir o software
    2. Clicar em [ New Project ]
    3. Há duas formas de criar um projeto novo

       FORMA 1:
               Quando um ambiente não foi criado usando o comando mkvirtualenv

       1. Tela de entrada           = [ Location ] = inserir o nome do av
       2. Tela de entrada           = [ new environment ] = [ Base Interpreter ] = [ ... ]
       3. Select python interpreter = [ /usr/bin/python3.8 para /usr/local/bin/python3.8 ]

       FORMA 2:
               Quando um ambiente já foi criado usando o comando: [ mkvirtualenv ]

       1. Tela de entrada           = [ Location ] = inserir o nome do av
       2. Tela de entrada           = [ Existing Interpreter ] = [ ... ]
       3. Add Python Interpreter    = [ /usr/bin/python3.8 ]
    """
