

def softwares():
    """
    Baixar e instalar software MySQL community x64
    """


def procedimentos_instalar_mysql():
    """
    Na instalação, escolher instalação [ Custom ]
    Programar o instalador para baixar as seguintes ferramentas:

    MySQL Server 8.0.21 - x64
    MySQL Workbench 8.0.21 - x64
    MySQL Connector Python 8.0.21 - x64

    Durante a instalação, manter todas etapas como padrão
    Criar uma senha para o usuário [ root ] padrão do servidor MySQL
    Finalizar a instalação
    """


def registrar_mysql_bin():
    """
    Ir à rota padrão de instalação do mysql no Windows, na pasta de binários
    c:\program files\mysql\mysql server 8.0\bin [ ctrl + c ]

    No windows, seguir os seguinte passos:

    Win / este computador / botão direito / propriedades / configurações avançadas do sistema /
    variáveis de ambiente / path / editar / novo

    c:\program files\mysql\mysql server 8.0\bin [ ctrl + v ]
    """


def terminal_primeiro_acesso_user_admin():
    """
    mysql -u root -p

    Se o mysql estiver devidamente configurado, será apresentado o MySQL Monitor
    MySQL Monitor oferece o comando [ help ] para ter acesso a comandos de ajuda
    MySQL Monitor oferece o comando [ exit ] para deslogamento do mesmo
    """


def esclarecimentos():
    """
    O usuário [ root ] não é recomendável ser trabalho para bdd
    Uma melhor opção é criar um usuário comum separado e torná-lo admin
    """


def terminal_tornar_user_admin():
    """
    No terminal, como feito anteriormente, é preciso acessar o usuário admin [ root ]
    mysql -u root -p
    Estando logado no MySQL Monitor, usar os múltiplos comandos

    CREATE USER 'nome do usuário novo'@'localhost' IDENTIFIED BY 'senha desejada';
    GRANT ALL PRIVILEGES ON *.* TO 'nome do usuário novo' WITH GRANT OPTION;
    FLUSH PRIVILEGES;

    Os comandos acima convertem um usuário comum para ter privilégios de admin
    O usuário novo agora deve ser usado, ao invés do usuário [ root ]
    """


def deslogar_root_logar_user_novo():
    """
    Com o MySQL Monitor, caso deseje-se deslogar do usuário atual, digita-se [ exit ]
    Faça o login no MySQL Monitor com o novo usuário criado [ mysql -u nome do usuário novo -p ]
    Se o usuário novo foi devidamente configurado, o MySQL Monitor será carregado normalmente
    """


def comandos_mysql_de_utilidade():
    """
    SHOW DATABASES;                # Mostrar uma lista de todos os bdds disponíveis
    USE nome do bdd;               # Logar em um dos bdds disponíveis
    SHOW TABLES;                   # Mostrar todas as tabelas criados pelo bdd alvo
    SELECT * FROM nome da tabela;  # Mostrar tabelas das tabelas de um bdd alvo
    """
