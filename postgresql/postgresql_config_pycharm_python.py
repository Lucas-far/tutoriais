

def requisitos():
    """
    1. PostgreSQL
    2. Conta PostgreSQL, com usuário novo que não seja o [ postgres ], com privilégios de admin
    3. Linguagem de Programação (no meu caso, Python)
    4. IDE (no meu caso, Pycharm)
    """

def terminal():
    """
    1. pip install psycopg2-binary
    2. pip freeze > requirements.txt
    """

def settings():
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',  # mudar o último nome após o ponto, para o nome do bdd desejado
            'NAME': 'bddpostgresql',     # única chave com valor livre
            'USER': 'luksadmin',         # nome do usuário novo criado após a criação do usuário padrão 'root'
            'PASSWORD': 'passwort2772',  # senha configurada junto com o usuário novo
            'HOST': 'localhost',         # valor padrão
            'PORT': '5432',              # valor apdrão
        }
    }

def pgadmin4():
    """
    1. Abrir o software Pgadmin4
    2. Logar no usuário não root [ não postgres ]
    3. No painel do usuário: [ Databases ] [ botão direito ] [ create ] [ database... ]
    4. Na criação do bdd, é preciso apenas [ name = chave "NAME" da var DATABASES ]
    5. Save
    """

def deploy_heroku():
    """
    1. pip install dj-database-url
    2. pip freeze > requirements.txt
    3. import dj_database_url
    4. Comentar a var DATABASES criada anteriormente acima
    5. DATABASES = {'default': dj_database_url.config()}
    6. git init
    7. git status
    8. git add .
    9. git commit -m "deploy_initial_config" (repetir, caso demore demais...)
    10. git status
    11. heroku login
    12. heroku create av.sufixo desejado --buildpack heroku/python
    13. git push heroku master
    14. heroku run python manage.py migrate
    15. heroku run python manage.py createsuperuser
    """
