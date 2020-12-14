

def models():
    """"""
    # Chamar bdd de usuário padrão Django [ User ], ou outro, se tiver sido configurado
    "from django.contrib.auth import get_user_model"

    # Modelo
    """
    class Vehicle(models.Model):
        drivers = models.ManyToManyField(get_user_model())
        model = models.CharField('Modelo', help_text='máx. 50 chars', max_length=50)
    
        class Meta:
            verbose_name = 'Veículo'
            verbose_name_plural = 'Veículos'
    
        def __str__(self):
            return self.model
    """

def admin():
    """"""
    # Sabe-se que campos [ models.ManyToManyField ] não podem ser chamados diretamente no módulo [ admin ]
    # Ao invés disso, cria-se uma função, e o seu nome é inserido como string na var [ list_display ]
    # Através da função, os campos poderão ser vistos normalmente
    # Se você quiser que o campo venha em português, então há duas opções:
    #     criar a função em português
    #     chamar o nome da função com o método [ .short_description ] e passar o nome do valor do campo
    """
    from django.contrib import admin
    from .models import *
    
    @admin.register(Vehicle)
    class VehicleAdmin(admin.ModelAdmin):
        list_display = ('model', 'show_field_drivers')
        
    def show_field_drivers(self, object):
        return ', '.join([each_data.username for each_data in object.drivers.all()])
    show_field_drivers.short_description = 'Motoristas'
    """

def terminal():
    """"""
    # python manage.py runserver

def template_admin():
    """"""
    # No template admin, e acessar o bdd alvo [ Vehicle ], o campo [ models.ManyToManyField ] deve estar visível
