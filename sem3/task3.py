# 3. Напишите программу, которая определит позицию 
# второго вхождения строки в списке либо сообщит, что её нет.
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

""" my_list = ["we", "qwe", "asd", "zxc", "qwe", "ertqwe", "qwe"]
my_string = 'qwe'
count = 0
for i in range(0, len(my_list)):
    if my_list[i] == my_string:
        count = count + 1
        if count == 2:
            print(f'позиция {i} - {my_list[i]} - вхождение {count}')
if count < 2:
        print(-1) """


my_list_1 = ["qwe", "asd", "zxc", '', "ertqwe", 'qwe']
value = 'qwe1'
count = 0
n_bool = False
for i in range(len(my_list_1)):
    if value == my_list_1[i]:
        count += 1
if count == 2:
    print(i)
    n_bool = True
if n_bool == False:
    print('-1')
    