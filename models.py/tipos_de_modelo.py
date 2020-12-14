

def banco_de_dados_generico():
    sintaxe = 'm'
    obs1 = 'Criado no módulo [ models.py ] somente'
    obs2 = 'Necessita uma classe aninhada Meta com abstract = True'
    # todo...Importante
    obs3 = 'O programador já sabe os campos e valores'
    obs4 = 'Banco de dados com padrão público, para ser herdado por outros bancos de dados'

def banco_de_dados_comum():

    sintaxe = 'ma'
    obs1 = 'Criado no módulo     [ models.py ]'
    obs2 = 'Registrado no módulo [ admin.py  ]'
    # todo...Importante
    obs2 = 'O programador já sabe os campos e valores'
    obs3 = 'Os objetos são criados e salvos pelo programador'

def banco_de_dados_formulario():

    # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    sintaxe = 's_fvut'
    obs1 = 'Configuração de variável em      [ settings.py ] (comentada acima)'
    obs2 = 'Criado no módulo                 [ forms.py    ] + função self + objeto da classe EmailMessage'
    obs3 = 'Exportado para o módulo          [ views.py    ] + condições essenciais + função self'
    obs4 = 'Criação da rota no módulo        [ urls.py     ]'
    obs5 = 'Criação do template no diretório [ templates   ]'
    # todo...Importante
    obs6 = 'O programador já sabe os campos, mas NÃO sabe os valores'
    obs7 = 'Não é um banco de dados, e os campos são impressos no terminal do projeto'

def banco_de_dados_formulario_modelo():

    sintaxe = 'mafvut'
    obs1 = 'Criado no módulo                 [ models.py ]'
    obs2 = 'Registrado no módulo             [ admin.py  ]'
    obs3 = 'Exportado para o módulo          [ forms.py  ] + criação de classe ModelForm'
    obs4 = 'Exportado para o módulo          [ views.py  ] + condições essenciais + método de salvar'
    obs5 = 'Criação da rota no módulo        [ urls.py   ]'
    obs6 = 'Criação do template no diretório [ templates ]'
    # todo...Importante
    obs7 = 'O programador já sabe os campos, mas NÃO sabe os valores'
    obs8 = 'Os objetos são criados pelo programador (sempre) e salvos pelo programador (incomum) ou pelo cliente (comum)'

def banco_de_dados_user():

    sintaxe = 'vut'
    obs1 = 'Não é criado, apenas importado, pois ele já existe no framework Django'
    obs2 = 'Importação da classe User e a biblioteca messages (opcional) no módulo [ views.py  ]'
    obs3 = 'Criação das condições de validação do formulário no módulo             [ views.py  ]'
    obs4 = 'Criação da rota no módulo                                              [ urls.py   ]'
    obs6 = 'Criação do template no diretório                                       [ templates ]'
    # todo...Importante
    obs7 = 'O programador já sabe os campos, mas NÃO sabe os valores'
    obs8 = 'Os objetos já existem no framework e são salvos pelo programador (incomum) ou pelo cliente (comum)'
    obs9 = 'Para saber como fazer um, ver diretório: [ User ] e módulo [ add_novo_user.py ]'
