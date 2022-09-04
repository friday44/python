# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

""" num = int(input('Введите число от 1 до 7, обозначающее день недели: '))
if num == 6 or num == 7:
    print('выходной день')
else:
    print('будний день') """


# 2. Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# Это равенство верно при любых булевых X Y Z

for x in True, False:
     for y in True, False:
        for z in True, False:
            print((not(x or y or z)), (not(x) and not(y) and not(z)))


# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

""" x = int(input('Введите значение x (ненулевое): '))
y = int(input('Введите значение y (ненулевое): '))
if x > 0 and y > 0:
    print('I четверть')
elif x < 0 and y > 0:
    print('II четверть')
elif x < 0 and y < 0:
    print('III четверть')
elif x > 0 and y < 0:
    print('IV четверть') """


# 4. Напишите программу, которая по заданному номеру четверти, показывает 
# диапазон возможных координат точек в этой четверти (x и y).
""" num = int(input('Введите номер четверти (число от 1 до 4): '))
if num == 1:
    print('x > 0, y > 0')
elif num == 2:
    print('x < 0, y > 0')
elif num == 3:
    print('x < 0, y < 0')
elif num == 4:
    print('x > 0, y < 0') """


# 5. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

""" x1 = int(input('Введите х1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите х2: '))
y2 = int(input('Введите y2: '))
print(f'расстояние между точками  {round((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5, 2)}') """
