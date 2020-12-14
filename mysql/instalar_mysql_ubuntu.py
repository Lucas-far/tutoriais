

def fonte_do_tutorial():
    """
    Plataforma:  Udemy
    Curso:       Banco de dados SQL e NoSQL - do básico ao avançado
    Localização: Seção 8 - Aula 45
    """

def comandos_terminal_iniciais():
    """
    sudo apt update && sudo apt -y upgrade && sudo apt list --upgradable
    sudo reboot
    """

def instalar_servidor_mysql():
    """
    sudo apt install mysql-server
    """

def gerenciamento_servidor_mysql():
    """
    1 - sudo mysql                    #  Logar no console MySQL
    2 - help                          #  Lista de comandos do console MySQL
    3 - exit                          #  Sair do console MySQL
    4 - sudo systemctl status mysql   #  Verificar status do servidor mysql pós sua instalação
    5 - sudo systemctl enable mysql   #  Iniciar servidor MySQL com o sistema operacional
    6 - sudo systemctl disable mysql  #  Cancelar iniciar o servidor MySQL com o sistema operacional
    7 - sudo systemctl start mysql    #  Iniciar/reiniciar servidor MySQL
    8 - sudo systemctl stop mysql     #  Congelar servidor MySQL
    """

def configurar_servidor_mysql():
    """
    No terminal, usar comando [ sudo mysql_secure_installation ]
    Serão executadas perguntas sobre ferramentas, algumas para adicionar, outras para remover

    Validate Password Plugin  # Digitar 'y' ou 'n'
    Password                  # Digitar uma senha para o usuário 'root' do MySQL
    Anonymous user            # Digitar 'y'
    Login remotely            # Digitar 'y'
    Test database             # Digitar 'y'
    Privilege tables          # Digitar 'y'
    """

def alertas():
    """
    1 - Recomenda-se que o usuário root do MySQL não seja trabalhado
    2 - Uma melhor opção é criar um novo usuário comum, e dar privilégios de admin para ele
    3 - Para criar um usuário, é preciso estar logado no console MySQL (sudo mysql)
    """

def criar_user_novo_e_converter_para_admin():
    """
    1 - CREATE USER 'nome do usuário'@'localhost' IDENTIFIED BY 'senha desejada';
    2 - GRANT ALL PRIVILEGES ON *.* TO 'usuário criado'@'localhost' WITH GRANT OPTION;
    3 - FLUSH PRIVILEGES;
    """

def deslogar_user_root_e_logar_user_novo():
    """
    É preciso sair do console MySQL, então se estiver no console mysql, digite [ exit ]
    No terminal comum, digitar [ mysql -u nome do usuário novo -p ]
    """

def comandos_posterior_login_user_novo():
    """
    SHOW DATABASES;                  # Mostrar todos os bdds
    USE nome do bdd;                 # Acessar um bdd específico (se você está em outro bdd, ele será deslogado)
    SHOW TABLES;                     # Mostrar tabelas de um bdd (já estando logado em um bdd específico)
    SELECT * FROM tabela de um bdd;  # Consultar uma tabela específica
    SELECT * FROM sys_config;        # Exemplo do comando acima
    """

# todo...Importante (Instalação da ferramenta MySQL Workbench)

def download_mysql_workbench():
    """
    Google:      MySQL Workbench - MySQL
    Link direto: https://www.mysql.com/products/workbench/
        Download now -> selecionar OS -> Clicar na versão mais nova -> Download -> No thanks, just start my download
    """

def instalar_mysql_workbench():
    """
    A instalação é pelo instalador baixado, similar ao Windows, sem complexidade
    Abra o software baixado e clique em [ install ]
    Espere a instalação finalizar
    """
