'''Задача 5. Порядочные списки'''

print('Введите количество чисел в первой последовательности:')
N1 = int(input())
print('Введите количество чисел во второй последовательности:')
N2 = int(input())

list_1 = []
list_2 = []

if N1 > 0:
    print('Введите числа первой последовательности:')
for _ in range(N1):
    number_N1 = int(input())  # введенное число
    if number_N1 >= 0:
        list_1.append(number_N1)
if N2 > 0:
    print('Введите числа второй последовательности:')
for _ in range(N2):
    number_N2 = int(input())  # введенное число
    if number_N2 >= 0:
        list_2.append(number_N2)

print('Список всех этих чисел в порядке возрастания:')
list_1.extend(list_2)
list_1.sort()
print(list_1)

