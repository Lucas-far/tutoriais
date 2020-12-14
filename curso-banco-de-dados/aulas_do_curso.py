

def aula_4():
    """"""

    # O que pode ser um 'dado'?
    "valor destinado à um tipo de informação definida"

    # O que pode ser uma 'informação'?
    "nomemclatura dos dados para dar significado a eles, e assim forma uma tabela, ou bdd"

    # Há algum exemplo?
    dados = ('Lucas', 28, 41, 86, 'Alameda dos Coelhos')
    dados_com_info = {'cliente': 'Lucas', 'idade': 28, 'casa': 41, 'ddd': 86, 'bairro': 'Aladema dos colehos'}

    "Dados não parecem fazer sentido sem a presença de informação"
def aula_5():
    """"""

    # O que significa SQL?
    "Structured query language - Linguagem de consulta estruturada"

    # O que significa NoSQL?
    "Not only structured query language - Linguagem não apenas de consulta estruturada"

    # O que pode ser um SGBD?
    "Sistema Gerenciador de banco de dados (tanto para bdd relacional, quanto para bdd não relacional)"

    # O que pode ser considerado vantagem em bdd relacionais?
    "Os dados estão sob bom gerenciamento de validação, verificação, integridade, controle, recuperação, etc"

    # O que pode ser considerado desvantagem em bdd relacionais?
    "Pobreza em escalabilidade e particionamento"

    # O que pode ser considerado vantagem em bdd não relacionais?
    """
    Por ausentar de estruturação de tabelas com linhas e colunas, costumam ter mais performance
    Há uma boa escalabilidade e particionamento e replicação de dados
    """
    var = ('chave & valor', 'documentos', 'colunas', 'grafos')
def aula_6():

    # Quais bancos de dados relacionais são bem conhecidos?
    relacionais = (
        'MariaDB / MySQL (incluso no curso)', 'PostgreSQL  (incluso no curso)', 'SQLite  (incluso no curso)',
        'Oracle database', 'Microsoft SQL server', 'Teradata', 'INMDB2', 'Sybase', 'H2', 'Access', 'Apache Derby',
        'Hive', 'HyperSQL')
def aula_7():

    # Quais bancos de dados não relacionais são bem conhecidos?
    n_relacionais = (
        'CouchDB relax (incluso no curso)', 'FireBase (incluso no curso)', 'MongoDB   (incluso no curso)',
        'Redis (incluso no curso)', 'HBase', 'Cassandra', 'Neo4j', 'RavenDB', 'Membase', 'Elasticsearch',
        'Oracle coherence', 'ApacheSolr', 'Riak'
    )
def aula_11():

    aula = {
        (2_05, 4_00): 'Porque há modelagem de dados em bancos de dados?',
        (4_00, 4_45): 'Observação sobre os modelos de dados',
        (4_45, 5_00): 'Tipos de modelagem',
        (6_07, 7_15): 'Modelagem conceitual - parte 1',
        (7_15, 8_45): 'Modelagem conceitual e analista de sistemas',
        (8_45, 9_25): 'Modelagem conceitual - parte 2',
        (10_02, 11_22): 'Modelagem conceitual - forma textual',
        (11_25, 12_12): 'Modelagem conceitual - forma diagrama (DER/MER - Diagrama/Modelo entidade relacionamento)',
        (12_12, 12_33): 'Modelagem conceitual - forma diagrama de classe',
        (12_33, 12_50): 'Paradigmas de programação',
        (13_02, 13_40): 'DER/MER = independente de implementação',
        (14_00, 14_35): 'Modelagem lógica',
        (14_35, 15_57): 'Modelagem lógica - bdd não relacional',
        (15_57, 17_30): 'Modelagem lógica - exemplo',
        (17_30, 18_57): 'Modelagem lógica - exemplo 2 - pk - relacionamento',
        (18_57, 19_45): 'Modelagem lógica - exemplo 3 - pk',
        (19_45, 20_50): 'Modelagem Física',
        (21_00, 21_47): 'Exemplo de preparação de uma modelagem física - texto normal',
        (21_47, 23_30): 'Exemplo de preparação de uma modelagem física - código SQL',
        (23_57, 25_00): 'Entidade',                  # tabela / objeto
        (25_00, 26_10): 'Atributo',                  # coluna / campo
        (26_13, 27_55): 'Chave (pk = primary key)',  # identificador
        (27_55, 29_40): 'Relacionamento',            # 2 entidades, 1 atrib em comum, objetivos !=
        (29_40, 31_40): 'Chave estrangeira',         # execução prática do relacionamento entre entidades
        (31_40, 32_00): 'Graus de relacionamento e seus tipos',
        (32_00, 33_25): 'Relacionamento unário',     # entidade em relacionamento consigo (incomum)
        (33_25, 34_30): 'Relacionamento binário',    # 2 entidades, 1 atrib em comum, objetivos !=
        (34_30, 35_13): 'Relacionamento ternário',   # 2+ entidades, 1 atrib em comum, objetivos !=
        (36_00, 36_33): 'Cardinalidade máxima',
        (36_33, 38_45): 'Cardinalidade one-by-one (1:1)',         # 1 vendedor p/ 1 escritório e vice-versa
        (38_45, 40_38): 'Cardinalidade one-to-many (1:n) (1:*)',  # 1 vendedor p/ * clientes e 1 cliente p/ 1 vendedor
        (40_38, 43_35): 'Cardinalidade many-to-many (n:m)',  # 1 vendedor p/ * clientes e 1 cliente p/ * vendedores
        (43_35, 44_40): 'Cardinalidade mínima',
        (44_40, 47_13): 'Cardinalidade mínima',
        (47_13, 49_45): 'Formas de representação',  # Comuns: clássico & pé de galinha
        (49_45, 51_40): 'MySQL workbench como ferramenta de criação de modelagem',
        (52_15, 54_13): 'Resumo das etapas de modelagem em um diagrama pequeno',

        ('Resultado',):
        """
        Modelo de tarefa do usuário
            definição de regras e tecnologia (pelo analista de sistemas)
                relatório descritivo do processo da tarefa do ponto de vista do usuário
                
        Modelo conceitual
            regras de negócio
                ferramentas ou objetos, propriedades técnicas, processos, mapeamento do domínio do usuário
                
        Modelo lógico
            definição de regras e tecnologia
                definição de dados, funções e projeto de regras
                
        Modelo físico
            Implementação
                Pode representar tanto o projeto como a própria interface gráfica, o bdd e os programas
        """
    }
def aula_12():

    aula = {
        (35, 48): 'Normalização de dados - parte 1',
        (48, 1_31): 'Normalização de dados - tipos de dados buscados e definidos',
        (1_31, 2_13): 'Normalização de dados - parte 2',
        (2_44, 3_11): 'Objetivo importante da normalização de dados',
        (3_11, 4_27): 'Conclusão',
    }
