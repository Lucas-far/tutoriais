

def models_imports():
    """"""
    # 1 - Campo para upload de imagem
    # 2 - Método separador de string composta por traços
    # 3 - Não sei a utilidade, mas é importante
    """
    from stdimage import StdImageField
    from django.template.defaultfilters import slugify
    from django.db.models import signals
    """

def models():
    """"""
    # Cria-se um modelo bdd subjetivo (nesse contexto, um bdd para coletar dados e opiniões do usuário)
    """
    class AboutYou(Base):

        choices_gender = (('feminino', 'feminino'), ('masculino', 'masculino'), ('outro', 'outro'))
    
        full_name = models.CharField('Nome completo', max_length=170)
        gender = models.CharField('Gênero', choices=choices_gender, max_length=9)
        email = models.EmailField('E-mail', max_length=200)
        nationality = models.CharField('Nacionalidade', max_length=100)
        age = models.IntegerField('Idade')
        self_grade = models.DecimalField('Sua nota sincera auto-avaliativa', decimal_places=1, max_digits=2)
        passtime = models.CharField('Conte alguns de seus passatempos', max_length=500)
        brief_description = models.TextField('Conte algo sobre você')
    
        slug = models.SlugField('Slug', blank=True, editable=False, max_length=200)
    
        avatar = StdImageField(
            'Avatar',
            upload_to='database_user',
            variations={'Thumb': {'height': 500, 'width': 500, 'crop': True}}
        )
    
        class Meta:
            verbose_name = 'Bio do usuário'
            verbose_name_plural = 'Bios dos usuários'
    
        def __str__(self):
            return self.full_name
    """

def admin():
    """"""
    # Importa-se o bdd no módulo admin
    # Registra-se o banco de dados para exibição no template admin, com os campos desejados (todos, de preferência)
    """
    from .models import AboutYou
    @admin.register(AboutYou)
    class UserAdmin(admin.ModelAdmin):
        list_display = ('full_name', 'gender', 'email', 'nationality', 'age', 'self_grade', 'passtime',
                        'brief_description', 'avatar', 'slug', 'creation', 'update', 'availability')
    """

def forms():
    """"""
    # Cria-se um módulo forms
    # Importa-se o módulo models para o módulo forms
    # Cria-se uma classe model form de um, entre os bdds do módulo models
    # Essa classe só funciona com outra classe aninhada Meta, onde fornece-se o modelo e os campos
    # Com relação a classe model form, os campos passados, são aqueles cujo valor são gerados pelo usuário
    # Com relação a classe model form, os campos que geram valores automáticos, não devem ser inserido na classe
    # Levando isso em conta, os campos excluidos da adição foram: creation, update, availability
    """
    from .models import AboutYou
    class AboutYouModelForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ('full_name', 'gender', 'email', 'nationality', 'age', 'self_grade', 'passtime',
                      'brief_description', 'avatar')
    """

def views():
    """"""
    # Importar o módulo forms, e consequentemente, a classe model form criada anteriormente
    # Importar o método de mensagens do bootstrap
    # Importar o método redirecionados do Django (página de criação de uma conta, página principal, etc...)
    # Cria-se uma view, onde o formulário deve ter um objeto da classe model form, para representá-lo
    # Construir as condições apropriadas para o contexto do formulário
    """
    from .forms import AboutYouModelForm
    from django.contrib import messages
    from django.shortcuts import redirect
    
    def questionary_user(request):

        model_form = AboutYouModelForm(request.POST or None, request.FILES)
        if str(request.user) != 'AnonymousUser':
            if str(request.method) == 'POST':
                if model_form.is_valid():
                    model_form.save()
                    model_form = AboutYouModelForm()
                    messages.success(request, 'O Formulário foi enviado com sucesso. Obrigado!')
                else:
                    messages.error(request, 'Há algum erro no seu formulário.')
            else:
                model_form = AboutYouModelForm()
        else:
            request.error(request, 'Você precisa ter uma conta registrada para acessar esse formulário')
            return redirect('index')
    
        context = {'model_form': model_form}
    
        return render(request, 'questionary_user.html', context)
    """
def urls():
    """"""

    # Importar o método path para registrar rotas
    # Importar o módulo views e a view alvo, para que uma rota seja destinada à ela
    # Criar a rota pelo método path, para a view, que está recebendo um formulário
    """
    from django.urls import path
    from .views import questionary_user
    
    urlpatterns = [
        path('questionary-user', questionary_user, name='questionary-user'),
    ]
    """
def templates():
    """"""
    # A fazer...

def css():
    """"""
    # A fazer...
