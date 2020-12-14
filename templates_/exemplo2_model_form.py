

""" Exemplo do uso de um formulário, sem usar sintaxe Django no template """
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
    class Questionary(models.Model):

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
            upload_to='database_user',
            variations={'Thumb': {'height': 500, 'width': 500, 'crop': True}}
        )

        # self_grade = models.DecimalField('Sua nota sincera auto-avaliativa', decimal_places=1, max_digits=2)
        # passtime = models.CharField('Conte alguns de seus passatempos', max_length=500)

        class Meta:
            verbose_name = 'Questionário'
            verbose_name_plural = 'Questionários'

        def __str__(self):
            return self.full_name

    def slug_database_questionary(instance, **kwargs):
        instance.slug = slugify(instance.full_name)
    signals.pre_save.connect(slug_database_questionary, sender=Questionary)
    """
def admin():
    """"""
    """
    from .models import Questionary
    @admin.register(Questionary)
    class OtherAdmin(admin.ModelAdmin):
        list_display = ('full_name', 'gender', 'email', 'nationality', 'age', 'brief_description', 'avatar', 'slug')
    """
def views():
    """"""
    # O objeto do formulário é criado após as validações, somente
    # Não pode-se usar o método [ .is_valid() ]
    # Os parâmetros e dados request são usados
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
                print(tuple([('id = ', n, 'valor = ', item) for n, item in request.POST.items()]))

        return render(request, 'questionary_user.html')
    """
def urls():
    """"""
    """
    from .views import questionary_user

    urlpatterns = [path('questionary-user', questionary_user, name='questionary-user')]
    """
def head():
    """"""

    """
    <link
        crossorigin="anonymous"
        href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
        integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"
        rel="stylesheet">
    <link href="href="static/css/módulo.css" rel="stylesheet">
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
            <div class="col">
                <button class="btn btn-light">
                    <a class="tag-a" href="index.html">Voltar à página inicial</a>
                </button>
            </div>
        </div>
    </div>
    """
def body_parte2():
    """"""
    # Esqueleto do formulário
    # action=""                     [ nome do template que receberá o formulário ]
    # id=""                         [ id chamado no botão de submeter dados, ao final do formulário ]
    # enctype="multipart/form-data" [ o formulário terá upload de imagem, portanto esse atributo é necessário ]
    """
    <div class="container">
        <form class="form" action="template_form.html" id="this-form" enctype="multipart/form-data" method="post">
            <fieldset>
                <legend>Diga-nos sobre você</legend>
            </fieldset>
        </form>
    </div>
    """
# As partes seguintes são os campos, portanto, dentro da tag <fieldset></fieldset>
def body_parte3():
    """"""
    # Campo: nome
    """
    <div class="row">
        <div class="form-group ma mb">
            <label for="full_name">Nome completo</label>
            <input type="text" class="form-control" id="full_name" name="full_name">
        </div>
    </div>
    """
def body_parte4():
    """"""
    # Campo: email
    """
    <div class="row">
        <div class="form-group ma mb">
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" name="email">
        </div>
    </div>
    """
def body_parte5():
    """"""
    # Campo: nacionalidade
    """
    <div class="row">
        <div class="form-group ma mb">
            <label for="nationality">Nacionalidade</label>
            <input type="text" class="form-control" id="nationality" name="nationality">
        </div>
    </div>
    """
def body_parte6():
    """"""
    # Campo: idade
    """
    <div class="row">
        <div class="form-group ma mb">
            <label for="age">Idade</label>
            <input type="number" class="form-control" id="age" name="age" min="1" max="120">
        </div>
    </div>
    """
def body_parte7():
    """"""
    # Campo: texto
    """
    <div class="row">
        <div class="form-group ma mb col-8 col-sm-7 col-md-7 col-lg-7 col-xl-7">
            <label for="brief_description">Diga sobre você</label>
            <textarea class="form-control" id="brief_description" name="brief_description" rows="7" cols="40">Escreva aqui</textarea>
        </div>
    </div>
    """
def body_parte8():
    """"""
    # Campo: upload de imagem
    """
    <div class="row">
        <div class="form-group ma mb">
            <label for="avatar">Seu avatar</label>
            <input type="file" class="form-control-file" id="avatar" name="avatar">
        </div>
    </div>
    """
def body_parte9():
    """"""
    # Campo: escolhas
    """
    <div class="row">
        <div class="form-group ma mb">
            <label for="exampleFormControlSelect1">Gênero</label>
            <select class="form-control" id="exampleFormControlSelect1" name="gender">
                <option>escolher...</option>
                <option>feminino</option>
                <option>masculino</option>
                <option>outro</option>
            </select>
        </div>
    </div>
    """
def body_parte10():
    """"""
    # Botão que interage com um atributo [ id="" ] da tag do formulário
    """
    <div class="row">
        <div class="form-group ma mb">
            <button class="btn btn-dark" form="this-form" type="submit">Enviar</button>
        </div>
    </div>
    """
def body_scripts():
    """"""
    # Continuação da instalação do Bootstrap
    """
    <script
        crossorigin="anonymous"
        integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
        src="https://code.jquery.com/jquery-3.5.1.slim.min.js">
    </script>

    <script
        crossorigin="anonymous"
        integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx"
        src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js">
    </script>
    """
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
