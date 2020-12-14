

def pa_models():
    """"""

    # Métodos destinados para modelos de banco de dados
    """
    Modelo.objects.all()                     # Armazenamento de todos os objetos de um bdd
    Modelo.objects.count()                   # Retorno inteiro de quantos objetos há em um bdd
    Modelo.objects.filter(campo=valor)       # Acessar um objeto por um de seus campos (loop for necessário)
    Modelo.objects.filter(campo=valor).campo # Acessar um campo de um objeto após criar um objeto por um de seus campos
    Modelo.objects.get(campo=valor)          # Acessar um objeto por um de seus campos (loop for necessário)
    Modelo.objects.get(campo=valor).campo    # Acessar um campo de um objeto após criar um objeto por um de seus campos
    Modelo.objects.first()                   # Retorno do campo principal do primeiro objeto criado em um bdd
    Modelo.objects.last()                    # Retorno do campo principal do último objeto criado em um bdd
    var.id                                   # Retorna inteiro do número de um objeto de um bdd (loop for ou instanciação)
    var.pk                                   # idem do método acima
    var.campo = novo valor                   # Sintaxe de alteração de valor de um objeto
    var.save()                               # Salvar uma variável de objeto após adição ou alteração nela
    var.delete()                             # Deletar uma variável de objeto criada
    """
