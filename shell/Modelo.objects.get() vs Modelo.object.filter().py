

def exemplo():
    """"""
    # Passo 1
    """
    python manage.py runserver
    from pa.models import Vehicle
    
    var = Vehicle.objects.filter(id=1)
    var2 = Vehicle.objects.get(id=1)
    
    print(var)  <QuerySet [<Vehicle: Volkswagen Ultra>]>
    print(var2) <Vehicle: Volkswagen Ultra>
    """

    # Vantagem do método [ .filter() ] em relação ao método [ .get() ]
    # [ .filter() ] mostra o QuerySet
    "print(var.query)"

    # Vantagem do método [ .get() ] em relação ao método [ .filter() ]
    # Ele permite chamar os campos do modelo: nativos ou estrangeiros, assim como a possibilidade de editá-los
    # Lembrando que campos estrangeiros vêm de métodos como: [ OneToOneField ] ou [ ForeignKey ]
    """
    var2 = Vehicle.objects.get(model='Electus')
    var2.manufacturer.name  # campo estrangeiro
    var2.chassi.number      # campo estrangeiro
    var2.chassi             # campo nativo
    var2.manufacturer       # campo nativo
    var2.model              # campo nativo
    var2.price              # campo nativo
    
    var2.manufacturer.name = '5555555555555555'
    var2.save()
    var2.price = 91077
    var2.save()
    """
