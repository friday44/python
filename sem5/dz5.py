# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

""" text = 'Мы неабв очень не любим Питон иабв Джавабв абв'
text_find = 'абв'

my_list = text.split()
print(my_list)

new_list = [item for item in my_list if text_find not in item]
print(new_list) """

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют
# два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

""" n = 221

gamer_1 = input('Введите имя игрока 1: ')
gamer_2 = input('Введите имя игрока 2: ')
temp = random.randint(1, 2)
if temp == 1:
    current_gamer = gamer_1
while n > 0:
    print(f'Сейчас количество конфет: {n}')
    while True:
        num_minus = int(input(f'{current_gamer}, сколько конфет возьмете? (от 1 до 28): '))
        if num_minus >= 1 and num_minus <= 28:
            break
    n -= num_minus
    if current_gamer == gamer_1:
        current_gamer = gamer_2
    else:
        current_gamer = gamer_1

if current_gamer == gamer_1:
    current_gamer = gamer_2
else:
    current_gamer = gamer_1

print(f'Победил игрок {current_gamer}') """



# 3. Создайте программу для игры в "Крестики-нолики".

""" pos = list(range(1, 10))

def fild(pos):
    print(pos[0], pos[1], pos[2])
    print(pos[3], pos[4], pos[5])
    print(pos[6], pos[7], pos[8])


def input(x_or_o):
    valid = False
    while not valid:
        player_answer = int(input("Куда поставим " + x_or_o + "? "))
        pos[player_answer-1] = x_or_o
        valid = True

def check_win(pos):
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_coord:
        if pos[each[0]] == pos[each[1]] == pos[each[2]]:
            return pos[each[0]]
    return False

def main(pos):
    counter = 0
    win = False
    while not win:
        fild(pos)
        if counter % 2 == 0:
           input("X")
        else:
           input("O")
        counter += 1
        tmp = check_win(pos)
        if tmp:
            print(tmp, "победа!")
            win = True
            break
        if counter == 9:
            print("Партия окончена вничью!")
            break
    fild(pos)
main(pos)  """

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

""" s_input = 'dddaacccyyf'
s_output = ""
i = 0
while i < len(s_input):
    count = 1
    while i + 1 < len(s_input) and s_input[i] == s_input[i + 1]:
        count = count + 1
        i = i + 1
    s_output += str(count) + s_input[i]
    i = i + 1
print(s_output) """


s_input = '3d2a3c2y1f'
s_output = ''
s_input = list(filter(lambda x: int(x) if x.isdigit() else x, s_input))
i = 0
while i in s_input:
    if s_input.isdigit(i):
        temp = i
        del i
        s_output.append(temp+1 * i)
        i = i + 1
    else:
        s_output.append(i)
print(s_output)


