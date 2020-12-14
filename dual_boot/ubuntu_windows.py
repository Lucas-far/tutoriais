

def fonte():
    """ https://www.youtube.com/watch?v=aKKdiqVHNqw """

def requisitos():
    """
    Hardware  # Pendrive de pelo menos 8gb
    Software  # Rufus
    Software  # Iso do Ubuntu desktop
    """

def procedimentos_iniciais():
    """
    Conecte o dispositivo USB (que deve estar formatado)
    No windows 10, [ logo / win + r / msinfo32 ] para saber se a BIOS = UEFI
    """
    # Caso não seja, esse tutorial torna-se inútil

def software_rufus():
    """
    Iniciar software Rufus como administrador
    No campo [ dispositivo ], por padrão, o seu dispositivo usb já deve estar selecionado automaticamente
    No campo [ seleção de boot ], fornecer o caminho onde está o módulo do [ iso do Ubuntu ] baixado
    No campo [ esquema de partição ], escolher [ GPT ]
    Clicar no botão [ INICIAR ]
    Escolher opção [ gravar no modo imagem ISO ]
    """

def windows_gerenciamento_de_disco():
    """
    Logo / botão direito / gerenciamento de disco
    Em partição OS (C:) / botão direito / diminuir volume / 3a opção / 409600 / Diminuir
    Reiniciar a máquina
    """

def bios():
    """
    No reiniciamento, pressionar F12 (contexto do modelo da bios do meu laptop)
    Selecionar o dispositivo USB, onde foi alocado a imagem do Ubuntu
    O procedimento de instalação do Ubuntu iniciará
    """

def instalar_ubuntu():
    """
    Escolher [ Install Ubuntu ]
    Selecionar sua língua
    Escolher [ Normal installation ] [ Download updates ] [ Install third-party software ]
    Escolher [ Install Ubuntu alongside Windows ]
    Escolher Localização
    Configurar conta de usuário Ubuntu
    Ubuntu iniciará sua instalação (procedimento demorado)
    Ao final da instalação, será requisitado um reinicialização
    Na reinicialização, retire o flashdrive quando surgir o texto abaixo, e depois pressione ENTER:

    ========================================================
    Please, remove the medium installation, then press ENTER
    ========================================================

    Na inicialização, normalmente acontece uma atualização de software, recomenda-se aceitá-la
    Após a atualização, reinicia-se a máquina novamente, e Ubuntu está pronto para uso
    """
