

def fonte():
    """
    Curso  # Bancos de Dados SQL e NoSQL do básico ao avançado
    Seção  # Seção 13:Redis - Parte 1
    Aula   # 139. Instalação e Configuração no Linux
    """

def terminal():
    """
    sudo apt-get update
    sudo apt-get install build-essential -y
    """
    # sudo apt-get install build-essential -y
    "Pacote para compiladores de código em C, C++, bibliotecas de compartilhamento"

def browser():
    """
    Pesquisa # redis
    Website  # https://redis.io/

    Na página do software # downloads / stable version / download
    """

def ubuntu():
    """
    Botão direito / Extract Here
    Renomear diretório para [ Redis ]
    """

# Se no seu OS, em /home/, não há essa pasta, crie-a
def ubuntu_dir_apps():
    """ Recortar o diretório [ Redis ] do diretório de [ Downloads ] para [ apps ] """

# todo -> Instalação do Redis na versão Console

def ubuntu_dir_redis():
    """
    1. Entrar no diretório [ Redis ]
    2. Em qualquer área vazia, clique [ botão direito / open in terminal ]
    3. No terminal, digitar [ make ]
    4. Um procedimento de compilação ocorrerá (não é rápido)
    5. No terminal, digitar [ make test ]
    6. No terminal, digitar [ sudo apt-get install tcl 8.5 -y ] (muito demorado)
    7. No terminal, digitar [ make test ]
    8. Dentro do diretório [ redis ], há o diretório [ src ]. Abra-o.
    9. Procurar pelos módulos [ redis-cli ] & [ redis-server ]
    10. No diretório [ redis/src ] clique em algum espaço vazio [ botão direito / open in terminal ]
    11. No terminal, digitar [ cd /usr/local/bin/ ]
    12. No terminal, digitar [ sudo ln -s /home/lucas/apps/redis/src/redis-cli . ] para criar um link simbólico
    13. No terminal, digitar [ sudo ln -s /home/lucas/apps/redis/src/redis-server . ] para criar um link simbólico
    14. Feche o terminal
    15. Abra o terminal
    16. No terminal, digitar [ redis-cli --version ]
    17. No terminal, digitar [ redis-server --version ]
    """

# todo -> Instalação da interface gráfica do Redis

def browser2():
    """
    Pesquisa # p3x redis ui / redis ui
    Website  # https://www.electronjs.org/apps/p3x-redis-ui

    1. Na lateral esquerda da tela do website, clique no link onde está a palavra [ repository  ]
    2. O link do repository é [ github.com/patrikx3/redis-ui ], adicione [ /releases ] ao link
    3. Aparentemente, deve-se escolher a opção [ P3X-Redis-UI-2020.10.499.AppImage ]
    4. Faça o download dessa opção
    """

def ubuntu_dir_downloads():
    """
    1. Mover o executável do diretório [ Downloads ] para o diretório [ apps ]
    2. Em algum local vazio do diretório [ apps ], fazer [ botão direito / Open in Terminal ]
    """

def terminal2():
    """
    1. No terminal, fazer [ chmod +x P3X-Redis-UI-2020.10.499.AppImage ]
        1.1 A função deste comando é a conversão de um módulo alvo para ser um executável
        1.2 Pode-se digitar somente as iniciais do executável e apertar [ tab ], para auto-completar

    2. No terminal, fazer [ ./P3X-Redis-UI-2020.10.499.AppImage ]
    3. Será aberto a interface do bdd [ Redis ]
    4. Após a instalação da interface gráfica, ela pode ser acessada em [ Show applications ]
    """

def iniciar_redis():
    """
    1. Ir ao diretório [ apps ] [ redis ] [ src ] e em uma área vazia, fazer [ botão direito ] [ Open in Terminal ]
    2. No terminal, fazer [ ./redis-server ]
    """
