# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые
# возрастающую последовательность. Порядок элементов менять нельзя.

# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.

nlist = [2, 5, 2, 3, 4, 6, 1, 7]

# mylist = [nlist[0]]
# count = 0
# for i in range(len(nlist)):
#     if nlist[i] > nlist[count]:
#         mylist.append(nlist[i])
#         count = i

mylist = [nlist[i] for i in range(1,len(nlist)) if nlist[i]> max(nlist[0:i])]
mylist.insert(0, nlist[0])
print(mylist)

#mylist = [nlist[i] for i in range(len(nlist)) if nlist[i] > nlist[i -1]]