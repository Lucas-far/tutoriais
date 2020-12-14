

def settings():
    """"""
    """ EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' """

def forms_import():
    """"""
    # Imports
    """
    from django import forms
    from django.core.mail.message import EmailMessage
    """

def forms():
    """"""
    # Criação do modelo falso (que não salva em um bdd)
    # O que há nele? 1. vars tupla choices (opcional) / 2. campos / 3. def dos campos / 4. var objeto EmailMessage
    """
    class QuestionaryForm(forms.Form):

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

        choices_ny = (('não', 'não'), ('sim', 'sim'), ('talvez', 'talvez'))

        name = forms.CharField(label=_('Qual o seu nome?'))
        email = forms.EmailField(label=_('Qual o seu e-mail?'))
        state = forms.ChoiceField(label=_('Em qual estado do Brasil você mora?'), choices=choices_states)
        years = forms.IntegerField(label=_('Há quantos anos vive no Brasil?'))
        like = forms.CharField(label=_('O que o Brasil têm que você mais gosta?'))
        foreign_country = forms.CharField(label=_('Qual país(es) deseja conhecer?'))
        departure = forms.ChoiceField(label=_('Você deseja sair do Brasil?'), choices=choices_ny)

        def print_data_into_terminal(self):
            content = \
                f'''
                =====================
                Dados do questionário
                =====================
    
                Nome                             = {self.cleaned_data['name']}
                Email                            = {self.cleaned_data['email']}
                Estado do Brasil                 = {self.cleaned_data['state']}
                Anos morando no Brasil           = {self.cleaned_data['years']}
                O que gosta no Brasil            = {self.cleaned_data['like']}
                Países estrangeiros para visitar = {self.cleaned_data['foreign_country']}
                Deseja sair do Brasil?           = {self.cleaned_data['departure']}
                '''

            printer = EmailMessage(
                body=content,
                headers={'Reply-To': self.cleaned_data['email']},
                subject='Respostas do Questionário sobre o Brasil',
                to=('meu_email@domínio.com',),
                from_email='meu_email@domínio.com'
            )
            printer.send()
    """

def views():
    """"""
    # Importar o módulo forms
    # Criar a view, e a variável objeto que contêm o formulário
    # Construir as condições essenciais e chamar a função self criada anteriormente
    """
    from .forms import QuestionaryForm
    from django.contrib import messages
    
    def tell_about_brazil(request):

        form = QuestionaryForm(request.POST or None)
        if str(request.user) != 'AnonymousUser':
            if str(request.method) == 'POST':
                if form.is_valid():
                    form.print_data_into_terminal()
                    form = QuestionaryForm()
                    messages.success(request, 'O Formulário foi enviado com sucesso. Obrigado!')
                else:
                    messages.error(request, 'Há algum erro no seu formulário.')
            else:
                form = QuestionaryForm()
        else:
            messages.error(request, 'Você precisa criar uma conta para ter acesso a esse formulário')
            return redirect('index')
    
        context = {'form': form}
    
        return render(request, 'tell-about-brazil.html', context)
    """

def pa_urls():
    """"""
    """
    from django.urls import path
    from .views import *

    urlpatterns = [path('tell-about-brazil', tell_about_brazil, name='tell-about-brazil')]
    """

def templates():
    """"""
    # O template será planejado antes de ser postado

def css():
    """"""
    # O css será planejado antes de ser postado
