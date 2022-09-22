# 2. Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.

# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

incoming_list = [1, 2, 3, 5, 1, 5, 3, 10]
""" outcoming_list = [i for i in incoming_list if incoming_list.count(i) == 1]
print(outcoming_list) """

""" outcoming_list2 = list(filter(lambda x: incoming_list.count(x) == 1, incoming_list))
print(outcoming_list2) """

# list comperhesh
""" input_list = [1, 2, 3, 5, 1, 5, 3, 10]
res = [item for item in input_list if input_list.count(item) == 1] # записали в новый лист неповторяющиеся элементы
print(res) """

# filter
""" input_list = [1, 2, 3, 5, 1, 5, 3, 10]
res = list(filter(lambda x: input_list.count(x) == 1, input_list)) # можно записать итог в лист, можно в кортеж (tuple)
print(res) """

# map
""" input_list = ['432', 'tr', '34', 'jhb']
res = list(map(lambda x: int(x) if x.isdigit() else x, input_list))
print(res) """
