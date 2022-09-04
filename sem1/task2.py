# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

""" numbers = [1, 4, 432, 8, 7, 5, 23]
max_num = 0
for temp in numbers:
    if temp > max_num:
        max_num = temp
print(max_num) """

""" num_1 = int(input('Введите число 1: '))
num_2 = int(input('Введите число 2: '))
num_3 = int(input('Введите число 3: '))
num_4 = int(input('Введите число 4: '))
num_5 = int(input('Введите число 5: '))
max = num_1
if max < num_2:
    max = num_2
if max < num_3:
    max = num_3
if max < num_4:
    max = num_4
if max < num_5:
    max = num_5
print(max) """


""" # Создание списка данных через цикл for
# range(5) -> [0, 1, 2, 3, 4]
# range(5, 16) -> [5, 6, 7 ..., 13, 14, 15]
# range(1, 11, 2) -> [1, 3, 5, 7, 9]
my_list = []
for i in range(5):
    num = int(input('--> '))
    my_list.append(num)
print(my_list) """


""" # Решение через встроенную функцию
my_list = [1, 4, 8, 5, 7]
print(max(my_list)) """


# for со второго элемента (срез)

""" my_list = [3, 5, 1, 2, 8]
maxx = my_list[0]
for item in my_list[1:]:
    if item > maxx:
        maxx = item

print(maxx) """

# для поиска индекса максимального элемента
""" my_list = [3, 5, 1, 2, 8]
maxx = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] > maxx:
        maxx = i

print(maxx) """

my_list = [3, 5, 1, 2, 8]
maxx = my_list[0]
maxx_i = 0
for i in range(1, len(my_list)):
    if my_list[i] > maxx:
        maxx = my_list[i]
        maxx_i = i

print(maxx, maxx_i)