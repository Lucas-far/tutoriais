

def terminal():
    """
    pip install --upgrade pip
    pip install -r requirements.txt
    pip uninstall -r requirements.txt (aula 107) (51:00)
    pip install channels-redis
    pip install coverage
    pip install django
    pip install django-bootstrap4
    pip install django-channels
    pip install django-chartjs (aula 101)
    pip install django-stdimage
    pip install dj-static
    pip install geoip2 (aula 96)
    pip install gunicorn
    pip install model_mommy
    pip install psycopg2-binary
    pip install PyMySQL
    pip install reportlab (aula 105)
    pip install requests (aula 92)
    pip install textblob
    pip install virtualenv
    pip install virtualenvwrapper-win
    pip install WeasyPrint
    pip install whitenoise
    """

# Instruções sobre os códigos

def textblob():
    """"""
    # Instruções
    """
    from textblob import TextBlob
    var = TextBlob('Uma frase em língua portuguesa')
    var.translate(to='ar')
    var.translate(to='en')
    var.translate(to='es')
    var.translate(to='fr')
    var.translate(to='ru')
    var.translate(to='zh-CN')
    """

    # Também pode ser feito
    """ print(var.translate(to='en')) """
