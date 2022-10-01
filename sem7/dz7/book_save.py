import csv

# def log_data(entry):
#     with open('book.csv', 'a') as file:
#         file.write('{},\n'.format(entry))

def log_data(entry):
    with open('book.csv', 'a') as data:
        writer = csv.writer(data, delimiter = ';')
        writer.writerow(entry)