# 1. Вычислить число c заданной точностью *d*
# *Пример:*
# - при $d = 0.001, π = 3.141
""" import math
pi = str(math.pi)
#d = str(0.001)
d = input('введите точность: ')
l = len(d)
print(pi[0:l]) """

# 2. Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.
# "20" -> [2, 2, 5]
""" n = int(input('Введите n: '))

def find_div(n):
    dividers = []

    for i in range(2, n):
        while n % i == 0:
            n //= i
            dividers.append(i)
    return dividers

print(find_div(n)) """



# 3. Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

""" list = [5, 5, 4, 3, 2, 1, 1]
list_res = []

for i in list:
    cou = 0
    for j in list:
        if j == i:
            cou += 1
    if cou == 1:
        list_res.append(list[i])

print(list_res) """


# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
k = 5

for i in range(k, 0, -1):
        coef = random.randint(0, 10)
        if coef > 1:
            print(f'{coef}*x^{i} +', end = ' ')
            with open('file2.txt', 'a') as data:
                data.write(str(coef) + '*x^' + str(i) + ' + ')
        if coef == 1:
            print(f'x^{i} +', end = ' ')
            with open('file2.txt', 'a') as data:
                data.write('x^' + str(i) + '+')

coef = random.randint(0, 10)
print(f'{coef}*x +', end = ' ')
with open('file2.txt', 'a') as data:
    data.write(str(coef) + '*x + ')

coef = random.randint(0, 10)
print(f'{coef} = 0')
with open('file2.txt', 'a') as data:
    data.write(str(coef) + ' = 0\n')





# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.