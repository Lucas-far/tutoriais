

def esclarecimento():
    """"""
    # Contexto
    """
    1. Supondo que queira-se diminuir o conteúdo de um template.
    2. Uma opção viável é o uso do [ loop for ], mas há uma condição.
    3. O [ loop for ] só será útil caso já haja as informações textuais salvas em um bdd.
    4. Elas estando em um bdd, podem ser chamadas no template, pelo loop for, uma por uma.
    """

def models():
    """"""
    # Exemplo de um modelo que receberá dados textuais como valor
    # Esses dados textuais serão guardados em vars, que quando chamadas no template, substituirão os textos
    """
    class Services(models.Model):
        choices_services = (
            ('lni-cog', 'engrenagem'),
            ('lni-stats-up', 'planilha'),
            ('lni-users', 'pessoas'),
            ('lni-layers', 'arquivos'),
            ('lni-mobile', 'celular'),
            ('lni-rocket', 'foguete'),
        )
        category = models.CharField('Categoria de atuação', max_length=200)
        category_description = models.TextField('Descrição', default='Descrição')
        icon = models.CharField('Ícone símbolo', choices=choices_services, max_length=30)

        class Meta:
            verbose_name = 'Serviço'
            verbose_name_plural = 'Serviços'

        def __str__(self):
            return self.category
    """

def admin():
    """"""

    # Como padrão, após a criação de um modelo no módulo models, ele deve ser registrado no módulo admin
    """
    from .models import Services

    @admin.register(Services)
    class ServicesAdmin(admin.ModelAdmin):
        list_display = ('category', 'category_description', 'icon')
    """

def views():
    """"""

    # A view, nesse contexto, serve para criar a variável objeto de um bdd e passá-la no contexto do template
    """
    from .models import Services

    class ModeloTemplateView(TemplateView):
        template_name = 'nome_do_template.html'

        def get_context_data(self, **kwargs):
            context = super(ModeloTemplateView, self).get_context_data(**kwargs)
            context['services'] = Services.objects.all()
            return context
    """

def urls():
    """"""

    # A rota, serve para criar o caminho para chegar no template, que paresentará o conteúdo
    """
    from .views import ModeloTemplateView

    urlpatterns = [
        path('nome-da-rota', ModeloTemplateView, name='nome-da-rota')
    ]
    """

# Aqui começa o procedimento de redução de conteúdo...

def template_reduzido():
    """"""
    # 1. {% for field in services %}{% endfor %} = Loop for que faz a iteração com o bdd
    # 2. {%field%}       = variável interna que carrega cada objeto do bdd separadamente
    # 3. {%services%}    = variável externa que contêm todos os objetos de um bdd
    # 4. {{field.campo}} = variável interna que carrega cada objeto do bdd separadamente, com um campo especificado
    # 5. Lembrando novamente que, a redução só é possível caso haja um bdd das informações, que serão minimizadas
    # 6. Os números 2, 3 e 4, são as informações textuais compactadas em vars dentro do loop for
    """
    <div class="row">
        {% for field in services %}                                                                                   1
        <div class="col-md-6 col-lg-4 col-xs-12">
            <div class="services-item wow fadeInRight" data-wow-delay="0.3s">
                <div class="icon">
                    <i class="{{ field.icon }}"></i>                                                                  2
                </div>
                <div class="services-content">
                    <h3><a href="#">{{ field.category }}</a></h3>                                                     3
                    <p>{{ field.category_description }}</p>                                                           4
                </div>
            </div>
        </div>
        {% endfor %}                                                                                                  5
    </div>
    """

def template_original():
    """"""
    # 1. Note a diferença de tamanho do template que pode ser reduzida, apenas por ter sido criado um bdd
    """
    <section id="services" class="section-padding">
      <div class="container">
        <div class="section-header text-center">
          <h2 class="section-title wow fadeInDown" data-wow-delay="0.3s">Our Services</h2>
          <div class="shape wow fadeInDown" data-wow-delay="0.3s"></div>
        </div>
        <div class="row">
          <!-- Services item -->
          <div class="col-md-6 col-lg-4 col-xs-12">
            <div class="services-item wow fadeInRight" data-wow-delay="0.3s">
              <div class="icon">
                <i class="lni-cog"></i>
              </div>
              <div class="services-content">
                <h3><a href="#">Easy To Used</a></h3>
                <p>Ut maximus enim dolor. Aenean auctor risus eget tincidunt lobortis. Donec tincidunt bibendum gravida. </p>
              </div>
            </div>
          </div>
          <!-- Services item -->
          <div class="col-md-6 col-lg-4 col-xs-12">
            <div class="services-item wow fadeInRight" data-wow-delay="0.6s">
              <div class="icon">
                <i class="lni-stats-up"></i>
              </div>
              <div class="services-content">
                <h3><a href="#">Awesome Design</a></h3>
                <p>Ut maximus enim dolor. Aenean auctor risus eget tincidunt lobortis. Donec tincidunt bibendum gravida. </p>
              </div>
            </div>
          </div>
          <!-- Services item -->
          <div class="col-md-6 col-lg-4 col-xs-12">
            <div class="services-item wow fadeInRight" data-wow-delay="0.9s">
              <div class="icon">
                <i class="lni-users"></i>
              </div>
              <div class="services-content">
                <h3><a href="#">Easy To Customize</a></h3>
                <p>Ut maximus enim dolor. Aenean auctor risus eget tincidunt lobortis. Donec tincidunt bibendum gravida. </p>
              </div>
            </div>
          </div>
          <!-- Services item -->
          <div class="col-md-6 col-lg-4 col-xs-12">
            <div class="services-item wow fadeInRight" data-wow-delay="1.2s">
              <div class="icon">
                <i class="lni-layers"></i>
              </div>
              <div class="services-content">
                <h3><a href="#">UI/UX Design</a></h3>
                <p>Ut maximus enim dolor. Aenean auctor risus eget tincidunt lobortis. Donec tincidunt bibendum gravida. </p>
              </div>
            </div>
          </div>
          <!-- Services item -->
          <div class="col-md-6 col-lg-4 col-xs-12">
            <div class="services-item wow fadeInRight" data-wow-delay="1.5s">
              <div class="icon">
                <i class="lni-mobile"></i>
              </div>
              <div class="services-content">
                <h3><a href="#">App Development</a></h3>
                <p>Ut maximus enim dolor. Aenean auctor risus eget tincidunt lobortis. Donec tincidunt bibendum gravida. </p>
              </div>
            </div>
          </div>
          <!-- Services item -->
          <div class="col-md-6 col-lg-4 col-xs-12">
            <div class="services-item wow fadeInRight" data-wow-delay="1.8s">
              <div class="icon">
                <i class="lni-rocket"></i>
              </div>
              <div class="services-content">
                <h3><a href="#">User Friendly interface</a></h3>
                <p>Ut maximus enim dolor. Aenean auctor risus eget tincidunt lobortis. Donec tincidunt bibendum gravida. </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    """
