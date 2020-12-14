

def terminal():
    """
    pip install django django-stdimage
    """


def pp_settings():
    """
    INSTALLED_APPS = ['stdimage']
    """


def pa_models():
    """
    class Bdd(models.model):
        image = StdImageField(
            'Imagem',
            upload_to='nome_da_pasta',
            variations = {'Thumb': {'height': int, 'width': int, 'crop': True}}
        )
    """
