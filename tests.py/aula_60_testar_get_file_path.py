

def models():
    """"""
    # Função no módulo [ models ]
    """
    from uuid import uuid4
    def get_file_path(_instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return filename
        
    """

def exemplo():
    """"""
    # Testando a função [ get_file_path() ]
    """
    import uuid
    from django.test import TestCase
    from model_mommy import mommy
    from pa.models import get_file_path
    
    class GetFilePathTestCase(TestCase):
        def setUp(self):
            self.var = f'{uuid.uudi4()}.png'
        def test_get_file_path(self):
            var = get_file_path(None, 'teste.png')
            self.assertTrue(len(var), len(self.var)) 
    """

def executar():
    """"""
    # Comandos para teste
    """
    coverage run manage.py test
    coverage report
    
    coverage html
    python -m http.server
    """
