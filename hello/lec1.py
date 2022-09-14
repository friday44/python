# print('hello world')

# типы данных и переменные 
# int, float, boolean, str, list, None

""" a = 123
b = 1.23
print(type(a))
print(type(b))

s = 'hello world'
# s = 'hello \nworld' # с переносом строки
print(s) #вывод строки

print(a, '-',b, '-', s)
print('{} - {} - {}'.format(a, b, s)) #форматированный вывод
print(f'{a} - {b} - {s}') # интерполяция строк

f = True
print(f)

list = ['1', '2', '3', 'hello', 1, 2, 4.5, True]
print(list)

col = ['hello', 1, 2, 4.5, True]
print(col) """

# ввод и вывлд данных
# print, input

""" print('Введите a')
a = float(input())
print('Введите b')
b = float(input())
print(a, '+',b, '=', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}') """

# Арифметические операции
# +, -, *, /, %, //(деление в целых числах), **(возведение в степень)
# **, 

""" a = 1.31231223
b = 3
c = round(a * b, 5)
print(c)

# (), Сокращенные операции
a = 3
a = a + 5
a += 5
print(a) """

# Логические операции
# >, <, >=, <=, ==, !=
# not, and, or (не путать с &, |, ^)
# is, is not, in, not in
# gen

""" f = 1 > 2 or 4 < 6
print(f) """

""" from re import T """


""" f = [1,2,3,4]
print(f)
print(not 2 in f) """

""" is_odd = not f[0] % 2
print(is_odd) """

# Циклы
# 
""" a = int(input('a= '))
b = int(input('b= '))
if a > b:
    print(a)
else:
    print(b) """

""" username = input('Введите имя: ')
if username == 'Маша':
    print('Привет, Маша!')
elif username == 'Юра':
    print('Юра - молодец!')
elif username == 'Ильнар':
    print("О, Ильнар")
else:
    print('Привет,', username) """

# Управляющие конструкции
# while
""" original = 234
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted) """

# Управляющие конструкции
# for
""" for i in range(1, 10, 2):
    print(i)

for i in 'qwe - rty':
    print(i) """


# Текст
""" text = 'съешь ещё этих мягких французских булок'
print(len(text))         #39 
print('ещё' in text)     #True
print(text.isdigit())    #False
print(text.islower)      #True
print(text.replace('ещё', 'ЕЩЁ')) #замена
print(text[0])      # c
print(text[1])      # ъ
print(text[len(text)])      # ошибка
print(text[len(text)-1])      # к
print(text[-5])      # к
print(text[:])      # печать всего text
print(text[2:]5)      # 
for c in text:
    print(c) """

# Списки: введение
# 

""" numbers = [1, 2, 3, 4, 5]
print(numbers)             # [1, 2, 3, 4, 5]

numbers = list(range(1, 6))
print(numbers)             # [1, 2, 3, 4, 5]

numbers[0] = 10
print(numbers)             # [10, 2, 3, 4, 5]

for i in numbers:
    i *= 2
    print(i)               # [20, 4, 6, 8, 10]
print(numbers)             # [10, 2, 3, 4, 5] """


""" colors = ['red', 'green', 'blue']
for e in colors:
    print(e)       # red green blue
for e in colors:
    print(e*2)     # redred greengreen blueblue
colors.append('gray')    # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red')    # del colors[0] # удалить элемент """

# Функции
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

"""arg = 2.3
print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType """