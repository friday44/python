# дз4. 3. Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

""" list = [5, 5, 4, 3, 2, 1, 1]
list_res = [i for i in list if list.count(i) == 1]
print(list_res) """


# дз3. 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# - [1.1, 1.2, 3.1, 10.01] => 0.19

""" list = [1.1, 1.2, 3.1, 10.01]
list_2 = list(map(lambda x: (x * 100 % 100), list))
print((max(list_2) - min(list_2)) / 100) """


# дз2. 2. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# Пример:
# - 0,56 -> 11
""" n = input('Введите число: ').split('.')
print(sum(map(int, n[1]))) """


# дз2. 3. Задайте список из k чисел последовательности (1 + 1 \ k) ^ k и выведите на экран их сумму
""" k = int(input('Введите целое число: '))
print(sum((1 + 1 / i) ** i for i in range(1, k + 1))) """

# дз3. 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12
""" lst = [2, 3, 5, 9, 3]
print(sum(lst[i] for i in range(1, len(lst), 2))) """