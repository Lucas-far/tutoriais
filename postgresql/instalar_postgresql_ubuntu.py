

def fonte():
    """
    Banco de dados SQL e NoSQL - do básico ao avançado
    Seção 8:PostgreSQL - Parte 1
    75. Instalação e Configuração no Linux
    """

def atualizar():
    """
    sudo apt update && sudo apt -y upgrade && sudo apt list --upgradable
    sudo reboot
    """

def instalar_parte1():
    """
    Instruções de instalação do site PostgreSQL para Linux [ Ubuntu ]
    https://www.postgresql.org/download/linux/ubuntu/

    sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    sudo apt-get update
    """

def comandos_condicionais():
    """
    Se após os 3 comandos anteriores, haver um erro de arquitetura [ i386 ], então fazer os códigos

    Se   [ dpkg --print-foreign-architectures ] == i386, então continuar
    Se   [ dpkg --print-architecture ]          == amd64, então continuar
    Usar [ sudo dpkg --remove-architecture i386 ]
    """

def instalar_parte2():
    """
    sudo apt-get -y install postgresql-12
    sudo apt-get -y install pgadmin4
    """

def terminal_postgresql():
    """
    sudo su - postgres  # logar no postgresql com a conta padrão admin [ postgres ]
    psql                # usar o console psql em uma conta já logado [ no contexto: postgres ]
    help                # buscar comandos auxiliares
    \q                  # deslogar a conta
    exit                # deslogar do postgresql
    """

def user_admin_adicionar_senha():
    """
    O usuário padrão admin [ postgres ] não vêm com uma senha configurada. Vamos fazer isso

    sudo su - postgres
    ALTER user postgres WITH PASSWORD 'senha desejada';  # Retorno = ALTER ROLE
    \q
    exit
    """

def criar_user_novo_converter_para_admin():
    """
    sudo su - postgres
    psql
    CREATE USER nome do usuário novo WITH PASSWORD 'senha desejada';
    ALTER USER nome do usuário novo WITH SUPERUSER;
    \q
    exit
    """

def usar_pgadmin4_com_user_novo():
    """
    1. Pgadmin4 é o software gerenciador para bdds do postgresql
    2. Instalação: [ sudo apt-get -y install pgadmin4 ]

    No Pgadmin4 -> [ Servers ] [ botão direito ] [ Create ] [ Server ]
    Na aba [ General ] [ Name = pode ser um nome qualquer ou um nome igual a chave NAME na var DATABASES ]
    Na aba [ Connection ] [ host = localhost ] [ Username = nome do usuário novo ] [ Password = senha do usuário novo ]
    """
