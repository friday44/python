# 2. Для натурального n создать последовательности 3n + 1.
# *Пример:*
# - Для n = 6:
# 1: 4,
# 2: 7,
# 3: 10,
# 4: 13,
# 5: 16,
# 6: 19

n = int(input("Введите число: "))

# for i in range(1, n + 1):
#     n = (3 * i + 1)
#     print(f'{i}: {n}')

i = 1
while i <= n:
    result = 3 * i + 1
    print(f'{i}: {result}')
    i += 1