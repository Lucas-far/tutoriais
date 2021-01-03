

def fonte():
    """
    Curso # Programação Web com Python e Django framework: Essencial
    Local # Seção 9:Relacionamentos entre modelos
    Aula  # 81. Relacionamento Um para Muitos
    """

def models():
    """
    class Manufacturer(models.Model):
        name = models.CharField('Nome', help_text='máx 50 chars', max_length=50)

        class Meta:
            verbose_name = 'Fabricante'
            verbose_name_plural = 'Fabricantes'

        def __str__(self):
            return self.name

    class Vehicle(models.Model):
        name = models.CharField('Modelo', help_text='máx. 50 chars', max_length=50)
        price = models.DecimalField('Preço', decimal_places=2, help_text='máx. 7 dígitos e 2 casas decimais', max_digits=9)

        class Meta:
            verbose_name = 'Veículo'
            verbose_name_plural = 'Veículos'

        def __str__(self):
            return self.name
    """

    # Na aula anterior, foi criado um modelo [ Vehicle ], vamos adicionar o campo [ name ] do modelo [ Manufacturer ]
    # Isso acontece por método [ models.ForeignKey ]
    # O novo modelo [ Manufacturer ] é criado acima do modelo [ Vehicle ], pois o que passa herança, fica acima
    # A função __str__ do modelo [ Vehicle ] também é modificada
    """
    class Vehicle(models.Model):
        manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
        
        def __str__(self):
            return f'{self.manufacturer} {self.model}'
    """

def admin():
    """"""
    # Registro do modelo [ Manufacturer ]
    """
    @admin.register(Manufacturer)
    class ManufacturerAdmin(admin.ModelAdmin):
        list_display = ('name',)
    """

    # Edição do modelo [ Vehicle ] = adição do nome do campo estrangeiro herdado do modelo [ Manufacturer ]
    """
    list_display = ('manufacturer')
    """

# Essa parte do terminal não é obrigatória
# Quando edita-se tabelas já criadas, pode haver conflitos
# A escolha do professor para resolver o conflito está descrita na função [ terminal ], abaixo
# No contexto dessa aula, foi a adição do campo [ manufacturer ] que gerou conflito

# Outra recomendação
# Em caso de conflito, o campo conflitante deve receber parâmetros como [ blank=True ] ou [ default='' ]
# manufacturer = models.ForeignKey(Manufacturer, blank=True, on_delete=models.CASCADE)
# manufacturer = models.ForeignKey(Manufacturer, default='Honda', on_delete=models.CASCADE)

def terminal():
    """
    ls
    rm db.sqlite3
    cd pa
    cd migrations
    rm 00*
    cd ..
    cd ..
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    """
