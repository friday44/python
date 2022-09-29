def find_data(find_str):
    # path = 'book.txt'
    data = open('book.txt', "r")
    for line in data:
        result = []
        if find_str in line:
            result.append(line)
        else:
            result.append('Не найдено')
    data.close()
    return result
