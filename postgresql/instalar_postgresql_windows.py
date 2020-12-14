

def fonte():
    """
    Banco de dados SQL e NoSQL - do básico ao avançado
    Seção 8:PostgreSQL - Parte 1
    74. Instalação e Configuração no Windows
    """

def software():
    """
    Baixar e instalar software PostgreSQL x64 para OS Windows
    https://www.postgresql.org/download/windows/
    """

def instalar_mysql():
    """
    1. Na instalação, será requisitado a instalação de softwares essenciais, dentre eles:

    PostgreSQL server
    Pgadmin4
    Stack Builder       # Software que disponibiliza mais ferramentas para PostgreSQL
    Command line tools

    2. Também será requisitado a configuração de uma senha para o usuário admin padrão [ postgres ]
    """

def registrar_postgresql_bin():
    """
    1. Ir à rota padrão de instalação do postgresql no Windows, na pasta bin
    c:\Program Files\PostgreSQL\12\bin [ ctrl + c ]

    2. No windows, seguir os seguinte passos:

    Win / este computador / botão direito / propriedades / configurações avançadas do sistema /
    variáveis de ambiente / path / editar / novo

    c:\Program Files\PostgreSQL\12\bin [ ctrl + v ]
    """

def terminal_primeiro_acesso_postgresql():
    """
    1. psql -U postgres
    2. Será requisitada a senha do usuário admin [ postgres ], que foi criada durante a instalação
    3. Ao fornecer a senha, o terminal retornará o Console psql
    4. Porém a melhor maneira de uso do PostgresSQL é pela sua aplicação web [ Pgadmin4 ]
    5. Pgadmin4 é instalado durante a instalação do software postgresql
    """

def acesso_pgadmin4():
    """
    1. Abrir o software [ Pgadmin4 ]
    2. Na abertura, sempre será requisitado a senha criada durante a instalação, do usuário admin postgres
    3. Ao fornecer a senha criada na instalação, vá ao canto superior esquerdo do Pgadmin, em [ Browser ] [ Servers ]
    4. Ao clicar em [ Servers ], clique em [ PostgreSQL 12 ]
    5. Será requisitado a senha criada na instalação novamente, forneça-a
    """

def esclarecimentos():
    """
    1. São necessárias duas requisições de senha
    2. A primeira requisição é a senha da sua conta microsoft, para ter ao painel do Pgadmin4
    3. A segunda requisição é a senha para logar na conta admin [ postgres ]
    """

def criar_user_novo_e_tornar_admin():
    """
    1. Após as duas requisições, torna-se disponível a opção [ Login/Group Roles ]
    2. Em [ Login/Group Roles ] botão direito [ Create ] [ Login/Group Role... ]

    Na aba [ General ]    -> [ name ]     = nome do usuário novo
    Na aba [ Definition ] -> [ password ] = senha do usuário novo
    Na aba [ Privileges ] -> [ Can login  = Yes ] [ Superuser = Yes ]

    3. Terminada a configuração, clique em [ Save ]
    """

def deletar_servidor_inicial_configurar_novo():
    """
    1. No canto superior esquerdo do Pgadmin4, na área de [ Browser ] [ Servers ] [ PostgreSQL 12 ]
    2. Botão direito em [ PostgreSQL 12 ] [ Remove server ] [ Yes ]
    3. Botão direito em [ Servers ] [ Create ] [ Server ]

    Na aba [ General ]    -> [ campo name ]     = Nome desejado qualquer
    Na aba [ Connection ] -> [ campo host ]     = localhost
    Na aba [ Connection ] -> [ campo Username ] = nome do usuário criado em [ Login/Group Role... ]
    Na aba [ Connection ] -> [ campo Password ] = senha do usuário criado em [ Login/Group Role... ]

    4. Terminada a configuração, clique em [ Save ]
    """
