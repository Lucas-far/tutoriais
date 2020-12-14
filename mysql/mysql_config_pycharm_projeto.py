

def requisitos():

    req1 = 'ter o MySQL instalado no OS, e ter configurado, um usuário "não root" com privilégios de admin'
    req2 = 'ter o MySQL Workbench instalado, pois é nele que será criado um banco de dados'
    req2 = 'ter o python instalado e configurado'
    req3_opcional = 'ter o Pycharm instalado e configurado'

def terminal():

    obs1 = 'Após criar um novo ambiente virtual, é preciso instalar um pacote'
    pacote = 'pip install PyMySQL'
    motivo = 'Esse pacote funciona como um driver de conexão entre o Python e MySQL'
    obs2 = 'O banco de dados MySQL não funciona com a hospedagem do Heroku, tornando o deploy inacessível'

def pp_settings():
    """
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # mudar o último nome após o ponto para: .tipo de bdd
            'NAME': 'bddmysql',          # nome do banco de dados a ser criado
            'USER': 'luksadmin',         # nome do usuário novo criado após a criação do usuário padrão 'root'
            'PASSWORD': 'passwort2772',  # senha configurada junto com o usuário novo
            'HOST': 'localhost',         # valor padrão
            'PORT': '3306',              # valor apdrão
        }
    }
    """

def mysql_workbench():

    passo1 = 'Abrir o software MySQL workbench'
    passo2 = 'Logar no usuário específicado na var DATABASES'
    passo3 = 'Ao logar, será aberto um documento Query, onde deve-se usar uma sintaxe específica para criar o bdd'
    passo4_sintaxe = 'CREATE DATABASE nome_do_bdd;'  # Normalmente = o que foi especificado em DATABASES.NAME
    passo5 = 'Clicar no ícone raio do Workbench'
    passo6 = 'No painel esquerdo da tela, atualize o [ SCHEMA ] para atualizar a adição do novo bdd'
