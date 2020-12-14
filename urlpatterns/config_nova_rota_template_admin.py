

def pp_urls():

    from django.contrib import admin
    from django.urls import path

    urlpatterns = [
        path('admin/', admin.site.urls)
    ]

    # Modifique o primeiro parâmetro [ 'admin/' ] para definir uma nova rota para o template administrativo
