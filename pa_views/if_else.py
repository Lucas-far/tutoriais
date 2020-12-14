

def exemplo_tipo_de_user():
    """
    if str(request.user) != 'AnonymousUser':
        if str(request.user.first_name) and str(request.user.last_name) != '':
            status = f'Usuário: {request.user.first_name} {request.user.last_name}'
        else:
            status = 'Usuário logado com dados não preenchidos'
    else:
        status = 'Usuário Anônimo'

    context = {
        'status': status
    }
    """


def exemplo_form():
    """
    questionary_var = QuestionaryForm(request.POST or None)

    if str(request.method) == 'POST':
        if questionary_var.is_valid():
            questionary_var.print_data_into_terminal()
            questionary_var = QuestionaryForm()
            messages.success(request, 'Formulário enviado com sucesso. Obrigado!')
        else:
            messages.error(request, 'Há algum erro no seu formulário')
    else:
        questionary_var = QuestionaryForm()

    context = {
        'questionary_var': questionary_var
    }
    """


def exemplo_model_form():
    """
    questionary_user_var = UserModelForm(request.POST or None, request.FILES)

    if str(request.method) == 'POST':
        if questionary_user_var.is_valid():
            questionary_user_var.save()
            questionary_user_var = UserModelForm()
            messages.success(request, 'O Formulário foi enviado com sucesso. Obrigado!')
        else:
            messages.error(request, 'Há algum erro no seu formulário.')
    else:
        questionary_user_var = UserModelForm()

    context = {
        'questionary_user_var': questionary_user_var
    }
    """

    # Na linha onde a variável é mesclada com o método .save(), poderia ser feito outro procedimento
    # Se a intenção não fosse salvar no bdd, o método seria modificado para .save(commit=False)
    # Também é possível criar uma variável, que é a mesclagem da variável do formulário com o método .save()
    # Essa variável conterá todos os campos e valores de um bdd específico
    # EX: var = questionary_user_var.save()
    # EX: print(var.full_name)
