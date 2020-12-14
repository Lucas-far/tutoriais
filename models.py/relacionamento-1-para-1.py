

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 9:Relacionamentos entre modelos
    Aula:   # 80. Relacionamento Um para Um
    """

def terminal():
    """
    pip install django
    django-admin startproject pp .
    django-admin startapp pa
    """

def settings():
    """
    INSTALLED_APPS = ['pa']
    TEMPLATES = [{'DIRS': ['templates']}]
    MEDIA_URL = '/media/'
    MEDIA_ROOT = path.join(BASE_DIR, 'media')
    STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
    """

def models():
    """"""
    # Primeiro modelo
    """
    class Chassi(models.Model):
        number = models.CharField('Chassi', help_text='máx. 16 chars', max_length=16)
    
        class Meta:
            verbose_name = 'Chassi'
            verbose_name_plural = 'Chassis'
    
        def __str__(self):
            return self.number
    """

    # Segundo modelo
    """
    class Vehicle(models.Model):
        chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
        model = models.CharField('Modelo', help_text='máx. 50 chars', max_length=50)
        price = models.DecimalField('Preço', decimal_places=2, help_text='máx. 7 dígitos e 2 casas decimais', max_digits=9)
    
        class Meta:
            verbose_name = 'Veículo'
            verbose_name_plural = 'Veículos'
    
        def __str__(self):
            return self.model
    """

def admin():
    """"""
    # Registro do modelo [ Chassi ]
    """
    from django.contrib import admin
    from .models import *
    
    @admin.register(Chassi)
    class ChassiAdmin(admin.ModelAdmin):
        list_display = ('number',)
    """

    # Registro do modelo [ Vehicle ]
    """
    from django.contrib import admin
    from .models import *
    
    @admin.register(Vehicle)
    class VehicleAdmin(admin.ModelAdmin):
        list_display = ('chassi', 'model', 'price')
    """

def terminal2():
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    """

def template_admin():
    """
    No modelo [ Chassi ] adiciona-se o primeiro objeto e salva-se ele
    Esse valor torna-se disponível no campo [ chassi ] do outro modelo [ Vehicle ], pois eles estão relacionados
    Que tipo de relação? relacionamento um por um
    Como é feita a relação? models.OneToOneField()
    No modelo [ Vehicle ] adiciona-se o primeiro objeto e salva-se ele
    No modelo [ Vehicle ], ao criar um segundo objeto, se a campo [ chassi ] repetir-se, haverá erro
    Por qual motivo? relacionamento um por um
    Um chassi por carro, um carro só pode ter um chassi
    """
    # No template admin ocorre a lógica por trás do relacionamento: um por um

def terminal_shell():
    """"""
    # Demonstração prática de: relacionamento 1 por 1 entre os modelos [ Chassi ] & [ Vehicle ]
    # No exemplo abaixo, foi usado o modelo [ Chassi ]
    # Note que, através do objeto do modelo [ Chassi ], que é [ var ], pode-se acessar campos nativos e estrangeiros
    """
    python manage.py shell
    from pa.models import *
    var = Chassi.objects.get(id=1)
    var.number          # campo nativo do modelo [ Chassi ]       
    var.vehicle.chassi  # campo estrangeiro do modelo [ Vehicle ]
    var.vehicle.model   # campo estrangeiro do modelo [ Vehicle ]
    var.vehicle.price   # campo estrangeiro do modelo [ Vehicle ]
    """

    # Demonstração prática de: relacionamento 1 por 1 entre os modelos [ Chassi ] & [ Vehicle ]
    # No exemplo abaixo, foi usado o modelo [ Vehicle ]
    # Note que, através do objeto do modelo [ Vehicle ], que é [ var ], pode-se acessar campos nativos e estrangeiros
    """
    python manage.py shell
    from pa.models import *
    var = Vehicle.objects.get(id=1)
    var.chassi.number  # campo estrangeiro do modelo [ Chassi ]
    var.chassi         # campo nativo do modelo [ Vehicle ]
    var.model          # campo nativo do modelo [ Vehicle ]
    var.price          # campo nativo do modelo [ Vehicle ]
    """
