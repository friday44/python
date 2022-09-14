# 2. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.
# ['65h34q', 'sdg634d', '147jnbv']
# "7"

""" my_list = ['65h734q', 'sdg634d', '147jnbv']
for i in my_list:
    if i.find('73') >= 0:
        print(i) """
 

""" list = ['65h34q', 'sdg634d', '147jnbv']
for i in list:
    if '7' in i:
        print(f'7 in {i}') """


n = 'h'
list = ['65h34q', 'sdg63h4d', '147jnbv']
def find_num(n, lst):
    res = []
    for i in lst:
        if n in i:
            res.append(i)
    return res
print(find_num(n, list))