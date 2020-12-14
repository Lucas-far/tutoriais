

def esclarecimentos():
    """"""

    """
    Ao executar esse algoritmo, os dados serão duplicados
    Ao executar esse algoritmo, é preciso deletar do template admin, os objetos antigos de ids desordenados
    Ao fazer isso, os objetos gerados pelo algoritmo com os ids corretos, são mantidos no bdd
    """

def terminal():
    """"""

    # lesser = menor id inteiro errado
    # bigger = maior id inteiro errado
    # target = número do id inteiro inicial que começará a reordenação

    # O algoritmo
    """
    python manage.py shell
    from pa.models import Modelo
    var = User.objects.all()
    lesser = 3
    bigger = 7
    target = 1

    while lesser < bigger:
        for each_data in var:
            each_data.id = target
            each_data.save()
            lesser += 1
            target += 1
    """
