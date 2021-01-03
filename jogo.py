

"""
Algoritmo
"""

"Parte 1"
# from random import choice
#
# counter = 0
# max_monthly_games_allowed = 12
# month_numbers = []
# box = set({})
# numbers = [*range(1, 26)]

"Parte 2"
# def choose_numbers():
#     global box, month_numbers
#     while len(box) < 15:
#         box.add(choice(numbers))
#     box = sorted(box)
#     month_numbers.extend(box)
#     box = set({})

"Parte 3"
# while counter < max_monthly_games_allowed:
#     choose_numbers()
#     counter += 1

"Resultado"
# print(month_numbers)

"Forma mais clara de mostrar o resultado"
# print('\n')
# for index, obj in enumerate(month_numbers):
#     index = index + 1
#     if not index % 15:
#         print(obj, end=' ')
#         print('\n')
#     else:
#         print(obj, end=' ')

from random import choice

box = set({})
numbers = [*range(1, 26)]
resultado = []

# jogos = [
#     1, 2, 4, 5, 6, 7, 8, 9, 15, 17, 20, 21, 23, 24, 25,
#     1, 5, 6, 8, 9, 10, 11, 13, 14, 15, 16, 21, 22, 23, 25,
#     2, 3, 6, 7, 9, 10, 15, 16, 19, 20, 21, 22, 23, 24, 25,
#     1, 4, 5, 6, 8, 10, 12, 15, 16, 17, 18, 20, 22, 23, 25,
#     1, 4, 5, 6, 7, 10, 11, 13, 14, 16, 17, 18, 19, 20, 23,
#     1, 2, 3, 5, 8, 9, 10, 12, 15, 16, 17, 19, 21, 23, 25,
#     3, 4, 5, 6, 7, 9, 13, 15, 16, 19, 21, 22, 23, 24, 25,
#     2, 4, 5, 7, 9, 14, 15, 16, 17, 18, 19, 20, 21, 22, 25,
#     1, 2, 3, 5, 6, 7, 8, 9, 12, 13, 15, 18, 21, 23, 24,
#     2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 21, 22, 25,
#     2, 3, 6, 8, 10, 12, 14, 15, 16, 18, 19, 20, 21, 23, 25,
#     2, 4, 7, 8, 9, 10, 13, 16, 17, 18, 19, 20, 21, 23, 25
# ]

jogos = [
    1, 3, 4, 5, 9, 10, 11, 14, 15, 18, 20, 21, 22, 23, 25
]

while len(box) < 15:
    box.add(choice(numbers))
box = sorted(box)
resultado.extend(box)
box = set({})
print(resultado)
