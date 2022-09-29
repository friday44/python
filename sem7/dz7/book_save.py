def log_data(entry):
    with open('book.txt', 'a') as file:
        file.write('entry {} \n'.format(entry))