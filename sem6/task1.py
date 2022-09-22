# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:*
# 1+2*3 => 7;
# (1+2)*3 => 9;

""" string = '1 + 2 * 3'.split()
for i in range(len(string)):
    if string[i].isdigit():
        string[i] = int(string[i])

op_1 = {'+': lambda x, y: x + y,
        '-': lambda x, y: x - y,}
op_2 = {'*': lambda x, y: x * y,
        '/': lambda x, y: x / y,}

e = 0
while ('*' in string) or ('/' in string):
    if string[e] in op_2:
        temp = op_2[string[e]](string[e - 1], string[e + 1])
        del string[e -1:e + 2]
        string.insert(e - 1,temp)
        e = 0
    else:
        e += 1

e = 0
while ('+' in string) or ('-' in string):
    if string[e] in op_1:
        temp = op_1[string[e]](string[e - 1], string[e + 1])
        del string[e -1:e + 2]
        string.insert(e - 1,temp)
        e = 0
    else:
        e += 1 

print(*string) """

a = ['412', '*', '123', '+', '412']
a = list(filter(lambda x: int(x) if x.isdigit() else x, a))
print(a)

