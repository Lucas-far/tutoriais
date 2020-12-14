

def terminal():
    """"""
    # Instalar / Salvar / Importar
    """
    pip install model_mommy
    pip freeze > requirements.txt
    from model_mommy import mommy
    """

def shell():
    """"""
    # Entrar
    """ python manage.py shell """

    # Importar
    """ from model_mommy import mommy """

    # Criar um objeto usando mommy
    # Os campos já existem, mas os valores não são definidos manualmente, então tornam-se valores aleatórios
    """ var = mommy.make('NomeDoBdd') """

    # Chamando campo do objeto criado (var.nome_do_campo)
    """ var.full_name """

    # Os objetos criados, podem ser editados normalmente
    """  
    obj = mommy.make('Address')
    obj.neighborhood
    obj.street
    obj.house
    obj.neighborhood = 'Shallow Wood'
    obj.street = 'Log street'
    obj.house = '11'
    obj.neighborhood.save()
    obj.street.save()
    obj.house.save()
    """

    # Caso queria criar múltiplos objetos para um modelo (a quantidade deve ser especificada)
    """ var = mommy.make('Address', _quantity=7) """

    # Múltiplos objetos são criados dentro de uma variável, e esta pode ser manipulada
    # Nesse exemplo, mostra-se a criação de 5 objetos aleatórios, e no loop while, todos são mostrados
    """ 
    var = mommy.make('Address', _quantity=5)
    index = 0
    while index < len(var):
        print(var[index].neighborhood, '\n', var[index].street, '\n', var[index].house)
        index += 1
    """
