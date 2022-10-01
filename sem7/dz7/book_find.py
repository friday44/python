import csv

# def find_data(find_str):
    
#     data = open('book.csv', "r")
#     for line in data:
#         result = []
#         if find_str in line:
#             result.append(line)
#         else:
#             result.append('Не найдено')
#     data.close()
#     return result

def find_data(find_str):
    with open('book.csv', "r") as data:
        reader = csv.reader(data, delimiter = ';')
        result = []
        for row in reader:
            if find_str in row:
                result.append(row)
            # else:
            #     result.append('Не найдено')
    data.close()
    return result

