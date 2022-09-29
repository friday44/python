def find_data():
    path = 'book.txt'
    data = open(path, "r")
    find_str = input('Введите слово для поиска: ')  
    for line in data:
        if find_str in line:
            print(line)
        else:
            print('Не найдено')
    data.close()
