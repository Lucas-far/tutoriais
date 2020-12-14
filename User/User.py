

def classe_user_no_shell():
    """"""
    # Importar
    """ 
    from django.contrib.auth.models import User
    from django.contrib.auth.models import UserManager
    """

    # Acessar métodos
    """
    python manage.py shell
    from django.contrib.auth.models import User
    dir(User)
    dir(UserManager)
    """

    # Criando novo objeto de usuário
    """
    new = User.objects.create_user(
        first_name='Cascão', last_name='Pereira', username='Cascudo', email='cascudo@gmail.com', password='blabla')
    new.save()
    """

    # Os campos do objeto podem ser chamados normalmente
    """
    new.first_name
    new.last_name
    ...
    """

    # Editando campos do novo usuário
    """ 
    new.first_name = 'Cebolinha'
    new.save()
    """
