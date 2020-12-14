

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 9:Relacionamentos entre modelos
    Aula:   # 82. Relacionamento Muitos para Muitos
    """

def obs():
    """ Esse script é uma continuação do módulo [ relacionamento-1-para-muitos.py ] """

def relacionamento_muitos_para_muitos():
    """
    1. Um motorista pode dirigir muitos veículos
    2. Um veículo podem ser dirigido por muitos motoristas
    """

def models():
    """"""
    # Para exemplificar o relacionamento: muitos para muitos, vamos usar o bdd User
    # OBS: Se houvesse um modelo de usuário customizado, ele seria chamado, ao invés do bdd padrão [ User ]
    "from django.contrib.auth import get_user_model"

    # Adiciona-se mais um campo ao modelo [ Vehicle ]
    # O primeiro modelo [ Chassi ]       representa: relacionamento 1 para 1            [ models.OneToOneField ]
    # O segundo modelo  [ Manufacturer ] representa: relacionamento 1 para muitos       [ models.ForeignKey ]
    # O terceiro modelo [ Chassi ]       representa: relacionamento muitos parar muitos [ models.ManyToManyField ]
    """
    class Vehicle(models.Model):
        drivers = models.ManyToManyField(get_user_model())
    """

def terminal2():
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    """

def template_admin():
    """"""
    # Há diferença na criação dos campos que têm relacionamento:
    # Relacionamento 1 para 1           = campo dropdown
    # Relacionamento 1 para muitos      = campo dropdown
    # Relacionamento muitos para muitos = campo dropdown exposto
    # Com o campo dropdown exposto, é possível escolher mais de uma opção
    # Campos [ models.ManyToManyField ] não podem ser registrados no módulo [ admin ]

def terminal():
    """"""
    # Como o campo [ models.ManyToManyField ] não pode ser visto diretamente no template admin
    # Nessa aula não é explicado a razão, mas pode ser vista pelo shell
    # Na próxima aula, que é 83, será explicado isso. Veja 
    # O loop for não é parte, mas serve para ter idéia de quando usar: [ first() ] [ get(id=int) ] ou [ last() ]
    # Para ver o valor do campo [ ManyToManyField ] é preciso uma sintaxe ordenada, que pode ser de 2 formas:
    # var.método().campoManyToManyField.método()
    # Modelo.método.método().método().campoManyToManyField.método()
    """
    python manage.py shell
    from pa.models import Vehicle
    all = Vehicle.objects.all()
    
    for index, object in enumerate(all):
        print(index, object.id, object.model)
    
    0 1 Mercedez Benz
    1 2 Ford Fusion
    2 3 Renault Logan
    
    all.first().drivers.all()    # <QuerySet [<User: Lucas>, <User: Santos>]>
    all.get(id=2).drivers.all()  # <QuerySet [<User: Lucas>, <User: Farias>]>
    all.last().drivers.all()     # <QuerySet [<User: Lucas>, <User: Santos>]>
    
    Vehicle.objects.all().first().drivers.all()    # <QuerySet [<User: Lucas>, <User: Santos>]>
    Vehicle.objects.all().get(id=2).drivers.all()  # <QuerySet [<User: Lucas>, <User: Farias>]>
    Vehicle.objects.all().last().drivers.all()     # <QuerySet [<User: Lucas>, <User: Santos>]>
    """
