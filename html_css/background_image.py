

def exemplo():
    """"""

    # Essa propriedade é uma incognita para mim, pois apresenta problemas que eu não compreendo
    # Em html normal, conectado à um css externo, não consigo fazer essa propriedade funcionar no Ubuntu
    # Em html com Django, a propriedade parece funcionar normalmente no Ubuntu
    # Tendo isso em mente, no caso de uso de html normal, recomenda-se o código abaixo em uma tag <style></style>

    """
    body {
        background-image: url('static/images/woods.png');
        background-attachment: fixed;
        background-size: cover;
        background-position: left;
    }
    """

    # background-image: url();       = chamar a rota da imagem para tornar-se plano de fundo
    # background-attachment: fixed;  = impedir que a imagem role junto com o conteúdo da página
    # background-size: cover;        = ajusta a imagem na tela
    # background-position: left;     = prioriza uma região da imagem, podendo ter até 2 valores (top right bottom left)
