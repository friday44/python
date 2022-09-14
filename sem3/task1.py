# 1. Реализуйте алгоритм задания случайных чисел 
# без использования встроенного генератора псевдослучайных чисел.

""" from time import time
sec = str(time())
num = sec[-1]
print(num) """


""" from random import random
import time
for i in range(10):
    num = time.time()
    print((int(num * 1000000))%10) """


""" import random
number = int(input('Введите число'))
indexs = []
for i in range(number):
    index = random.randint(0, number - 1)
    if index in indexs:
        while index in indexs:
            index = random.randint(0, number - 1)
indexs.append(index) """


""" import datetime
x = datetime.datetime.now()
rand_num = int(x.strftime("%f")) % 10
print(rand_num) """


