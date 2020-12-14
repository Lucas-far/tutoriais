

def remover_vogais(string):
    container = []
    vowels = ['a', 'e', 'i', 'o', 'u',
              'à', 'á', 'â', 'ã',
              'é',
              'í',
              'ó', 'ô', 'õ', 'ò'
              'ú',
              ]
    for lt in string:
        container.append(lt)
    for lt in vowels:
        while lt in container:
            container.pop(container.index(lt))
    container = ''.join(container)
    print(container)

remover_vogais('Maria do Rosário de Fátima Farias Santos / Lucas Farias Santos de Sousa')
