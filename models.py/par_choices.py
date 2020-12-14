

def conceito():
    """"""
    # [ choices=var ] é um parâmetro que recebe uma tupla com tuplas aninhadas, para criar campos dropdown
    # [ choices=var ] sempre recebe var tupla, e esta var tupla deve ser criada antes do campo que irá usá-la
    # [ choices=var ] sempre recebe var tupla, e esta var tupla recebe o prefixo [ choices ], para melhor identificação
    # [ choices=var ] requer também o parâmetro [ max_length=int ] cujo valor é = a string de maior número de caracteres

def exemplos():
    """"""
    # Exemplo 1 - criação de um campo dropdown dos estados do Brasil
    """
    choices_states = (
        ('Acre', 'Acre'), ('Alagoas', 'Alagoas'), ('Amapá', 'Amapá'), ('Amazonas', 'Amazonas'),
        ('Bahia', 'Bahia'), ('Brasília', 'Brasília'), ('Ceará', 'Ceará'), ('Espírito Santo', 'Espírito Santo'),
        ('Goiás', 'Goiás'), ('Maranhão', 'Maranhão'), ('Mato Grosso', 'Mato Grosso'),
        ('Mato Grosso do Sul', 'Mato Grosso do Sul'), ('Minas Gerais', 'Minas Gerais'),
        ('Paraíba', 'Paraíba'), ('Paraná', 'Paraná'), ('Pará', 'Pará'), ('Pernambuco', 'Pernambuco'),
        ('Piauí', 'Piauí'), ('Rio de Janeiro', 'Rio de Janeiro'), ('Rio Grande do Norte', 'Rio Grande do Norte'),
        ('Rio Grande do Sul', 'Rio Grande do Sul'), ('Rondônia', 'Rondônia'), ('Roraima', 'Roraima'),
        ('Santa Catarina', 'Santa Catarina'), ('São Paulo', 'São Paulo'), ('Sergipe', 'Sergipe'),
        ('Tocantins', 'Tocantins')
    )
    """

    # Exemplo 2 - criação de um campo dropdown para respostas curtas
    """ choices_ny = (('não', 'não'), ('sim', 'sim'), ('talvez', 'talvez')) """

    # Exemplo 3 - criação de um campo dropdown de escolha de gênero
    """ choices_gender = (('feminino', 'feminino'), ('masculino', 'masculino'), ('outro', 'outro')) """

def models():
    """"""
    # Na criação do modelo, a ordem dos fatores é:
    # 1. var tupla choices,
    # 2. var campo
    # 3. parâmetro da var campo
    """
    class States(models.Model):
        # 1
        choices_states = (
            ('Acre', 'Acre'), ('Alagoas', 'Alagoas'), ('Amapá', 'Amapá'), ('Amazonas', 'Amazonas'),
            ('Bahia', 'Bahia'), ('Brasília', 'Brasília'), ('Ceará', 'Ceará'), ('Espírito Santo', 'Espírito Santo'),
            ('Goiás', 'Goiás'), ('Maranhão', 'Maranhão'), ('Mato Grosso', 'Mato Grosso'),
            ('Mato Grosso do Sul', 'Mato Grosso do Sul'), ('Minas Gerais', 'Minas Gerais'),
            ('Paraíba', 'Paraíba'), ('Paraná', 'Paraná'), ('Pará', 'Pará'), ('Pernambuco', 'Pernambuco'),
            ('Piauí', 'Piauí'), ('Rio de Janeiro', 'Rio de Janeiro'), ('Rio Grande do Norte', 'Rio Grande do Norte'),
            ('Rio Grande do Sul', 'Rio Grande do Sul'), ('Rondônia', 'Rondônia'), ('Roraima', 'Roraima'),
            ('Santa Catarina', 'Santa Catarina'), ('São Paulo', 'São Paulo'), ('Sergipe', 'Sergipe'),
            ('Tocantins', 'Tocantins')
        )
        
        #        2                                    3
        states = models.CharField('Escolha o estado', choices=choices_states, max_length=19)
    
        class Meta:
            verbose_name = 'Estado'
            verbose_name_plural = 'Estados'
    
        def __str__(self):
            return self.states
    """
