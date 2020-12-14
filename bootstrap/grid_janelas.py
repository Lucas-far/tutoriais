

def tamanhos_de_janela():
    """"""
    # Lembrando que, são três divs, e na terceira costuma-se configurar o espaço ocupado:
    """
    Janela muito pequena = col-xm- / col- = 576px menos
    Janela pequena       = col-sm-        = 576px até 768px
    Janela média         = col-md-        = 768px até 992px
    Janela grande        = col-lg-        = 992px até 1200px
    Janela extra grande  = col-xl-        = 1200px até 1920px
    """

    # Exemplo
    """
    <div class="container">
        <div class="row">
            <div class="col col-sm- col-md- col-lg- col-xl-">
                <tag>Conteúdo</tag>
            </div>
        </div>
    </div>
    """
