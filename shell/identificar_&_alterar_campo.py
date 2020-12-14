

def contexto():
    """"""

    # Contexto
    """
    1. Supondo que uma pessoa esteja em um banco de dados
    2. first_name = 'Lucas'
    3. last_name = 'Farias'
    4. O problema é que eu quero mudar seu sobrenome, mas não lembro do valor
    5. A solução é criar um objeto dessa pessoa, com um campo que se saiba o valor, que é no caso: nome
    6. Então, ficaria assim:
    """

    # python manage.py shell
    # from pa.models import Staff
    # pessoa = Staff.objects.get(first_name='Lucas')     # forma 1
    # pessoa = Staff.objects.filter(first_name='Lucas')  # forma 2
    # pessoa.last_name = 'Sousa'
    # pessoa.save()

    """
    7. Eu pude mudar o sobrenome da pessoa, indiretamente, pois eu não sabia o valor do campo do sobrenome
    8. Então eu criei um objeto usando um campo cujo qual eu sabia o valor: nome
    9. E pela variável de objeto, eu chamei o campo que eu queria modificar e dei a ele um novo valor
    10. Por último, usando a variável do objeto com o método save(), salva-se a alteração feita
    """
