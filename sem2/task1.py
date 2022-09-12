# 1. Напишите программу, которая принимает на вход число N и
# выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81


""" num = int(input("Введите число: "))
numbers = [1]
for i in range(num - 1):
    n = (numbers[i] * -3)
    numbers.append(n)
print(numbers) """


num = int(input("Введите число: "))
n = 1
for i in range(num):
    print(n, end = ' ')
    n = (n * -3)
