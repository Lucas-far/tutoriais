
""" Exemplo do uso de um formulário, usando sintaxe Django no template """
def terminal():
    """"""

    """
    pip install bootstrap4
    pip freeze > requirements.txt
    """
def settings():
    """"""
    # {% load static %} só funciona se for configurado no módulo [ settings ]
    """
    INSTALLED_APPS = ['bootstrap4'] 
    STATIC_URL = '/static/'
    STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
    """
def models_imports():
    """"""
    """
    from stdimage import StdImageField
    from django.template.defaultfilters import slugify
    from django.db.models import signals
    """
def models():
    """"""
    """
    class Other(models.Model):

        choices_gender = (('feminino', 'feminino'), ('masculino', 'masculino'), ('outro', 'outro'))

        full_name = models.CharField('Nome completo', max_length=170, default='João Pereira')
        gender = models.CharField('Gênero', choices=choices_gender, max_length=9, default=None)
        email = models.EmailField('E-mail', max_length=200, default='email@domínio.com')
        nationality = models.CharField('Nacionalidade', max_length=100, default='Turco')
        age = models.IntegerField('Idade', default=18)
        brief_description = models.TextField('Conte algo sobre você', default='Escreva aqui.')
        slug = models.SlugField('Slug', blank=True, editable=False, max_length=200)

        avatar = StdImageField(
            'Avatar',
            upload_to='database_other',
            variations={'Thumb': {'height': 500, 'width': 500, 'crop': True}}
        )

        # self_grade = models.DecimalField('Sua nota sincera auto-avaliativa', decimal_places=1, max_digits=2)
        # passtime = models.CharField('Conte alguns de seus passatempos', max_length=500)

        class Meta:
            verbose_name = 'Outro'
            verbose_name_plural = 'Outros'

        def __str__(self):
            return self.full_name

    def slug_database_other(instance, **kwargs):
        instance.slug = slugify(instance.full_name)
    signals.pre_save.connect(slug_database_other, sender=Other)
    """
def admin():
    """"""
    """
    from .models import Other
    @admin.register(Other)
    class OtherAdmin(admin.ModelAdmin):
        list_display = ('full_name', 'email', 'nationality', 'age', 'brief_description', 'avatar', 'gender', 'slug')
    """
def views():
    """"""
    # No módulo [ views ] é que nota-se a diferença
    # O objeto do formulário é criado após as validações, somente
    # Não pode-se usar o método [ .is_valid() ]
    # Os parâmetros são usados visivelmente, além dos dados request
    """
    from .models import Other

    def questionary_user(request):

        if str(request.method) == 'POST':
            if request.POST['full_name'] and request.POST['email'] and request.POST['nationality'] \
             and request.POST['age'] and request.POST['brief_description'] and request.FILES['avatar'] \
             and request.POST['gender'] != '':
                var = Other(
                    full_name=request.POST['full_name'],
                    gender=request.POST['gender'],
                    email=request.POST['email'],
                    nationality=request.POST['nationality'],
                    age=request.POST['age'],
                    brief_description=request.POST['brief_description'],
                    avatar=request.FILES['avatar'],
                    slug=request.POST.get('slug')
                 )
                var.save()
                # print(tuple([('id = ', n, 'valor = ', item) for n, item in request.POST.items()]))
        return render(request, 'questionary_user.html')
    """
def urls():
    """"""
    """
    from .views import questionary_user

    urlpatterns = [path('questionary-user', questionary_user, name='questionary-user')]
    """
def declarar():
    """"""
    """
    {% load static %}
    {% load bootstrap4 %}
    """
def head():
    """"""

    """
    {% bootstrap_css %}
    <link href="{% static 'css/módulo.css' %}" rel="stylesheet"> <!-- href="static/css/módulo.css" -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title></title>
    """
def body_parte1():
    """"""
    # Botão para voltar à página inicial
    """
    <div class="container">
        <div class="row">
            <div class="col ma">
                <button class="btn btn-light">
                    <a href="{% url 'index' %}">Voltar à página inicial</a>
                </button>
            </div>
        </div>
    </div>
    """
def body_parte2():
    """"""
    # {% bootstrap_form var %} pode ser adaptada em tags com classe bootstrap
    """
    <div class="container">
        <form class="form" action="{% url 'questionary-user2' %}" enctype="multipart/form-data" id="this-form" method="post">
            <fieldset>
                <legend>Diga-nos sobre você</legend>
                {% csrf_token %}
                {% bootstrap_messages %}
                <div class="row">
                    <div class="col-8 col-sm-7 col-md-6 col-lg-5 col-xl-4 ma mb">
                        {% bootstrap_form questionary_user_var %}
                        {% buttons %}
                            <button class="btn btn-dark" form="this-form" type="submit">Enviar</button>
                        {% endbuttons %}
                    </div>
                </div>
            </fieldset>
        </form>
    </div>
    """
def body_declarar():
    """"""
    """ {% bootstrap_javascript jquery='full' %} """
def css():
    """"""
    """
    body {background-color: #222; color: #00b489;}
    .btn-light {margin: 25px 0 50px 0;}
    .btn-light:hover a {text-decoration: none;}
    form {border: #292929 solid 1px; padding: 10px;}
    .ma {margin: auto;}
    .mb {margin-bottom: 20px;}
    legend {font-size: 2em; padding: 10px 0 20px 10px;}
    .form-control {background-color: #171A21;}
    .form-control:focus {background-color: #171A21;}
    """
