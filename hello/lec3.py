# Анонимные, lambda функции

""" # def sum(x, y):
#     return x+y

sum = lambda x, y: x+y  # это то же самое, что выше

def mult(x, y):
    return x+y

def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)

    calc(mult, 4, 5)

    calc(lambda x, y: x+y, 4, 5) # это еще проще """

# List Comprehension
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

""" list = []
for i in range(1, 21):
    if i%2 == 0:
        list.append(i)
print(list) """

#равноценная запись в формате List Comprehension
""" list = [i for i in range(1, 21) if i%2 == 0]
print(list) """

#получение пар чисел (кортежей)
""" list = [(i, i) for i in range(1, 21) if i%2 == 0]
print(list) """

# подключим функцию, выведем кубы чисел из списка
""" def f(x):
    return x**3
list = [f(i) for i in range(1, 21) if i%2 == 0]
print(list) """

# к предыдущей записи подключим кортежи
""" def f(x):
    return x**3
list = [(i, f(i)) for i in range(1, 21) if i%2 == 0]
print(list) """

""" import numbers

path = 'file4.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e**2))
print(out) """


#Анонимные, lambda функции 
""" def select(f, col):
    return [f(x) for x in col]
def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()
data = select(int, data)
data = where(lambda e: not e % 2, data)
data = list(select(lambda e: (e, e**2), data)) """

# Функция map
# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.

""" li = [x for x in range(1, 20)]
li = list(map(lambda x:x+10, li))
print(li) """


# Функция filter
# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.

""" data = [x for x in range(10)]
res = list(filter( data))
print(res) """

# наш примерчик
""" data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: not x%2, res))
print(res) """


# Функция zip
# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора
# zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
#  ↓
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# Нельзя пройтись дважды



# Функция enumerate
# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
#  ↓
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды