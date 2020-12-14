

def teoria():
    sintaxe = '{% block content %}{% endblock %}'
    utilidade = 'É usado no template matriz para restringir parte do seu conteúdo, que será herdado'

    sintaxe2 = "{% extends 'template_matriz.html' %}"
    utilidade2 = 'É usado em um template herdeiro, que receberá o conteúdo do template matriz'

    sintaxe3 = '{% block content %}{% endblock %}'
    utilidade3 = 'É usado no template herdeiro para armazenar o seu próprio conteúdo, independente do template matriz'

def template_matriz():

    # Há 3 tags <section>, mas a última é restringida de ser herdada

    esqueleto = \
        """
        <section>
            <h2>Nome</h2>
            <p>Lucas Farias Santos de Sousa</p>
        </section>
    
        <section>
            <h2>Idade</h2>
            <p>28 anos</p>
        </section>
    
        {% block content %}
            <section>
                <h2>Nacionalidade</h2>
                <p>brasileiro</p>
            </section>
        {% endblock %}
        """

def template_herdeiro():

    # O template herdeiro terá tudo do template matriz, com exceção o que foi restringido pelo {% block content %}
    # O template herdeiro possui seu conteúdo independente dentro do {% block content %}

    esqueleto = \
        """
        {% extends 'template_matriz.html' %}
        {% block content %}
            <section>
                <h2>Profissão</h2>
                <p>Programador</p>
            </section>
        {% endblock %}
        """
