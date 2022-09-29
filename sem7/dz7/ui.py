def get_comand():
    print('1 - добавление записи в книгу')
    print('2 - поиск записи в книге')
    return input('Введите номер операции: ')

def get_data():
    book_entry = []
    book_entry.append(input('Введите фамилию: '))
    book_entry.append(input('Введите имя: '))
    book_entry.append(input('Введите номер телефона: '))
    book_entry.append(input('Введите описание: '))
    return book_entry

def get_find_string():
    return input('Введите слово для поиска: ')

def print_data(data):
    print(data)