# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 4 5

""" f1 = open('file7.txt', 'r')
output1 = f1.read()
nlist = output1.split()
print(nlist)

# for i in range(1, len(nlist)):
#     if int(nlist[i]) - 1 != int(nlist[i-1]):
#             numb = int(nlist[i]) - 1

# print(numb)

mylist = [int(nlist[i])-1 for i in range(1, len(nlist)) if int(nlist[i]) - 1 != int(nlist[i-1])]
print(mylist) """

with open('file7.txt', 'r') as f:
    string = f.readline()

string = string.split()
string = list(map(int, string))

for i in range(1, len(string)):
    if string[i] - 1 != string[i - 1]:
        print(f'пропущено число {string[i] - 1}')
        break