

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 9:Relacionamentos entre modelos
    Aula:   # 83. Aproveitando os recursos do Django Models
    """

def obs():
    """"""
    # Durante as aulas 80, 81 e 82, foram criados três modelos
    # Classificações desses modelos
    """
    Modelo [ Chassi ]       = entidade forte = independente
    Modelo [ Manufacturer ] = entidade forte = independente
    Modelo [ User ]         = entidade forte = independente (não foi criado, mas foi herdado)
    Modelo [ Vehicle ]      = entidade fraca = depende dos modelos [ Chassi ], [ Manufacturer ] e [ User ]
    """

    # Por qual razão o modelo [ Vehicle ] depende dos outros?
    "Pelo fato dele ter recebido como herança, os campos dos outros modelos, e não o inverso"

    # Como ocorreu essa herança?
    """
    A herança do modelo [ Chassi ]       para [ Vehicle ] foi [ models.OneToOneField ]
    A herança do modelo [ Manufacturer ] para [ Vehicle ] foi [ models.ForeignKey ]
    A herança do modelo [ User ]         para [ Vehicle ] foi [ models.ManyToManyField ]
    """

    # O que acontece quando se há herança entre modelos?
    """
    Cria-se um vínculo entre os objetos dos bdds: tanto do bdd [ provedor ] quanto do bdd [ herdeiro ]
    Já sabe-se que [ Chassi ] é um [ bdd provedor ] e [ Vehicle ] é um [ bdd herdeiro ]
    Vamos criar um contexto:
        1. No modelo [ Chassi ], há apenas 1 campo, chamado [ number ], e ele possui vários valores adicionados
        2. Dentre os valores, vamos supor que eu tenha o valor = 1234567
        3. No modelo [ Vehicle ] há um campo herdado, chamado [ chassi ], que é o campo [ number ] do modelo [ Chassi ]
        4. No modelo [ Vehicle ], ao criar um objeto, o valor do campo herdado, [ chassi ] = 1234567
        5. Se por acaso eu, deletar, do modelo [ Chassi ], do campo [ number ], o valor = 1234567
        6. O objeto do modelo [ Vehicle ], no campo [ chassi ], que recebeu o valor = 1234567, também será deletado 
        7. Afinal de contas, eles foram vínculados: 
            7.1. [ Modelo provedor ] Modelo [ Chassi ] e campo [ number ] 
            7.2. [ Modelo herdeiro ] Modelo [ Vehicle ] e campo [ chassi ]
    """

    # Por qual motivo isso acontece?
    """
    Por dois motivos
        1. Por estarem vínculados a relacionamentos
        2. Pelo fato de ser mandatório, ter o parâmetro [ on_delete= ] na criação do campo
            2.1 Normalmente esse parâmetro é configurado como [ on_delete=models.CASCADE ]
    """

    # Todos os relacionamentos são afetados da mesma forma?
    """
    Não, apenas 2/3
        1. Relacionamento 1 para 1           [ models.OneToOneField ]       é afetado
        2. Relacionamento 1 para muitos      [ models.ForeignKey ]          é afetado
        3. Relacionamento muitos para muitos [ models.ManyToManyField ] não é afetado
    """

def terminal():
    """"""
    # Onde encontramos o [ models.CASCADE ] mencionado acima?
    """
    python manage.py shell
    from django.db import models
    dir(models)
    """

# todo -> SOLUÇÃO 1

def models():
    """"""
    # [ models.CASCADE ] pode, por exemplo, ser substituido por:
    """ 
    class Vehicle(models.Model):
        manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_DEFAULT, default=1) 
    """

    # Qual a lógica aqui?
    """
    1. O modelo [ Manufacturer ] possui um campo [ name ]
    2. O modelo [ Vehicle ] herda do modelo [ Manufacturer ], o campo [ name ], mudando o nome para [ manufacturer ]
    3. O campo [ manufacturer ] é do tipo [ models.ForeignKey ] que demanda o parâmetro [ on_delete= ]
    4. Ao invés de usar o valor padrão para o parâmetro [ on_delete=models.CASCADE ], usa-se algo alternativo
    
    5. O que é esse algo alternativo?
        5.1. [ on_delete=models.SET_DEFAULT, default=1 ]
    
    6. O que isso significa?
        6.1. A tradução é longa...
        
        6.2. [ Manufacturer ] [ name ] [ Ford ]    = modelo / campo / objeto do modelo
        6.2. [ Manufacturer ] [ name ] [ Renault ] = modelo / campo / objeto do modelo
        6.2. [ Manufacturer ] [ name ] [ Citroën ] = modelo / campo / objeto do modelo
        6.2. [ Manufacturer ] possui apenas 1 campo, e ele gerou 3 objetos, nesse contexto
        6.2. [ Manufacturer ] gerou 3 objetos, todo objeto têm um id=int, então temos: id=1, id=2, id=3 
        
        6.3. [ Vehicle ] [ manufacturer ] [ Ford ] = modelo / campo herdado = campo / valor herdado = objeto do modelo
        
        6.4. Se eu for ao modelo [ Manufacturer ] e deletar o objeto [ Ford ]...
        6.4. Se eu for ao modelo [ Vehicle ], o objeto que recebeu [ Ford ] como valor, também será deletado
        
        6.5. Para evitar isso: [ on_delete=models.SET_DEFAULT, default=1 ]
        6.5. Ou seja, impedir o objeto do modelo herdeiro de ser deletado
        6.5. Ao invés disso, substitua o valor que não existe mais, pelo objeto do modelo provedor, que tenha id=1
        6.5. Qual objeto do modelo provedor que possui id=1? [ Ford ] 
    """
    # Obviamente, isso pode ser uma solução para um problema, ou não, vai depender muito do contexto

def terminal2():
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    """

# todo -> SOLUÇÃO 2

def models2():
    """"""
    # Qual a outra solução?
    """
    1. criar uma função para ser chamada no parâmetro [ on_delete= ] posteriormente
    2. A função vêm acima (antes e fora do escopo) da criação do modelo herdeiro [ Vehicle ]
    """

    # Como fazer isso?
    """
    def set_default_class_manufacturer():
        return Manufacturer.objects.get_or_create(name='Confidencial')[0]
    
    class Vehicle(models.Model):
        manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET(set_default_class_manufacturer))
    """

    # Para quê fazer isso?
    """
    1. Caso um objeto de um modelo provedor seja deletado, o objeto de um modelo herdeiro vinculado não seja também
    2. Ao invés disso, a função cria um objeto pré-definido e passa para modelo herdeiro, impedindo seu deletamento
    3. Por exemplo, se no modelo [ Manufacturer ] há um objeto = [ Ford ] e ele for deletado
    3. Este objeto será imediatamente substituido por outro objeto = [ Confidencial ]
    """

    # O que significa a sintaxe dessa função?
    # Manufacturer.objects.get_or_create(name='Confidencial')[0]
    """
    1. Modelo.método.método(campo='valor')[índice]
    2. Esse modelo [ Manufacturer ] possui e precisa de apenas um campo [ name ] para criar um objeto
    3. Então, está sendo criado um novo objeto para o modelo [ Manufacturer ] na execução da função
    """
