def log_data(entry):
    with open('book.txt', 'a') as file:
        file.write('{},\n'.format(entry))