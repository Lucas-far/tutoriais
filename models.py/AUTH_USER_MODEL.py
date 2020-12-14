

def fonte():
    """
    Curso:  # Programação Web com Python e Django framework: Essencial
    Local:  # Seção 7:Dissecando o Django User Model
    Aula:   # 67. Criando um User Model Customizado
    """

# Recomenda-se fazer isso em um novo projeto, para evitar problemas nos comandos de terminal

def settings():
    """"""
    # Configuração: var = av.nome do modelo customizado
    "AUTH_USER_MODEL = 'pa.MyCustomUser'"

def models_imports():
    """"""
    # Import 1: Customizador usuário com poucas funcionalidades
    # Import 2: Customizador usuário com mais funcionalidades
    # Import 3: Criar um gerenciador para o tipo de usuário do import 2
    """
    from django.contrib.auth.models import AbstractBaseUser
    from django.contrib.auth.models import AbstractUser
    from django.contrib.auth.models import BaseUserManager
    """

def models():
    """"""
    # models_def1() -> função executável para criar um novo usuário
    # models_def2() -> função configurada para criar um novo usuário normal
    # models_def3() -> função configurada para criar um novo usuário admin
    # use_in_migrations vêm de [ from django.contrib.auth.models import BaseUserManager ] [ dir(BaseUserManager) ]
    """
    class UserManager(BaseUserManager):
        use_in_migrations = True
    
        def1()
        def2()
        def3()      
    """

def def1():
    """"""
    # normalize_email() vêm de [ from django.contrib.auth.models import BaseUserManager ] [ dir(BaseUserManager) ]
    """
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('E-mail é um campo obrigatório')
        
        # corrigir erros gramaticais (letras cacha alta, caracteres especiais)
        email = self.normalize_email(email)  
        
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    """

def def2():
    """"""
    """
    def create_user(self, email, password=None, **extra_fields):
        # Comentado enquanto não há validação
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        
        return self._create_user(email, password, **extra_fields)
    """

def def3():
    """"""
    """
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Usuário não têm acesso à sessão administrativa')
        elif extra_fields.get('is_superuser') is not True:
            raise ValueError('Usuário não possui validação de admin')

        return self._create_user(email, password, **extra_fields)
    """

def models2():
    """"""
    # Outras sugestões de campo: rg / cpf
    """
    class MyCustomUser(AbstractUser):
        email = models.EmailField('Email', unique=True)
        phone_number = models.IntegerField('Telefone', max_length=15)
        is_staff = models.BooleanField('Membro da equipe', default=True)
    
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']
    
        def __str__(self):
            return self.email
    
        objects = UserManager()
    """

def forms_e_imports():
    """"""
    # pa/new/pythonfile/forms
    # Imports
    """
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth.forms import UserChangeForm
    from .models import *
    """

def form1():
    """"""
    """
    class MyCustomUserUserCreationForm(UserCreationForm):
        class Meta:
            model = MyCustomUser
            fields = ('first_name', 'last_name', 'phone_number')
            labels = {'username': 'Username/Email'}
    
        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['password1'])
            user.email = self.cleaned_data['username']
            if commit:
                user.save()
            return user
    """

def form2():
    """"""
    """
    class MyCustomUserUserChangeForm(UserChangeForm):
        class Meta:
            model = MyCustomUser
            fields = ('first_name', 'last_name', 'phone_number')
    """

def admin_imports():
    """"""
    """ 
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin 
    from .forms import MyCustomUserUserCreationForm, MyCustomUserUserChangeForm
    from .models import MyCustomUser
    """

def admin():
    """"""
    """
    @admin.register(MyCustomUser)
    class MyCustomUserAdmin(UserAdmin):
        add_form = MyCustomUserUserCreationForm
        form = MyCustomUserUserChangeForm
        model = MyCustomUser
        list_display = ('first_name', 'last_name', 'phone_number', 'email', 'is_staff')
    
        # fieldsets = ((classe, {'classe2': ('valor'),}))
        # fieldsets = dict(tuple(None or str, dict))
        fieldsets = (
            (None, {'fields': ('email', 'password')}),
            ('Informações pessoais', {'fields': ('first_name', 'last_name', 'phone_number')}),
            ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
            ('Datas importantes', {'fields': ('last_login', 'date_joined')})
        )
    """

def terminal():
    """"""
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    """
