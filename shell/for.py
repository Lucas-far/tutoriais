

def exemplos():
    """"""

    # Loop for pode ser útil para mostrar Querysets de um bdd (loop for normal, mostrando somente o campo __str__)
    """
    python manage.py shell
    from pa.models import Modelo
    var = Modelo.objects.all()

    for each_object in var:
        print(each_object)
    """

    # Loop for pode ser útil para mostrar Querysets de um bdd (loop for flexível, especificando os campos)
    """
    python manage.py shell
    from pa.models import Modelo
    var = Modelo.objects.all()
    
    for each_object in var:
        print(each_object.name, each_object.price, each_object.storage)
    """
