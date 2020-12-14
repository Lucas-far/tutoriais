

def a():
    """
    Sintaxe: <a>
    Tipo:    tag de linha
    Função:  criar texto link, que direciona para templates externos
    Obs:     a abertura do template pode ser ou não, na mesma página, pelo atributo [ target="_blank" ]
    """

def b():
    """
    Sintaxe: <b></b>
    Tipo:    tag de linha
    Função:  criar texto negrito, sem ênfase para motor de busca
    Obs:     para ênfase em motor de busca, usa-se <strong></strong>
    """

def br():
    """
    Sintaxe: <br>
    Tipo:    ausente
    Função:  criar uma quebra de linha (+ de 1 = espaçamento de linha)
    Obs:     pode ser substituida por {display: block; margin-bottom: intpx;}
    """

def em():
    """
    Sintaxe: <em></em>
    Tipo:    tag de linha
    Função:  criar texto itálico, com ênfase para motor de busca
    Obs:     para tirar ênfase em motor de busca, usa-se <i></i>
    """

def h1_h6():
    """
    Sintaxe: <h1></h1> até <h6></h6>
    Tipo:    tag de bloco
    Função:  criar títulos com variações de tamanho
    Obs:     quanto menor o número da tag, maior o tamanho do título
    """

def i():
    """
    Sintaxe: <i></i>
    Tipo:    tag de linha
    Função:  criar texto itálico, sem ênfase para motor de busca
    Obs:     para ênfase em motor de busca, usa-se <em></em>
    """

def ol():
    """
    Sintaxe: <ol></ol>
    Tipo:    tag de bloco
    Função:  criar lista ordenada, com padrão numérico (pode ser modificado)
    Obs:     é mandatório a tag <li></li> aninhada à essa tag
    """

def p():
    """
    Sintaxe: <p></p>
    Tipo:    tag de bloco
    Função:  criar parágrafo
    Obs:     ausente
    """

def strong():
    """
    Sintaxe: <strong></strong>
    Tipo:    tag de linha
    Função:  criar texto negrito, com ênfase para motor de busca
    Obs:     para tirar ênfase em motor de busca, usa-se <b></b>
    """

def ul():
    """
    Sintaxe: <ul></ul>
    Tipo:    tag de bloco
    Função:  criar lista não-ordenada, com padrão pontilhado (pode ser modificado)
    Obs:     é mandatório a tag <li></li> aninhada à essa tag
    """
