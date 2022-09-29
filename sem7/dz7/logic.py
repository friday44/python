import ui
import book_save as bs
import book_find as bf

def button_click():
    command = ui.get_comand()
    if command == '1':
        bs.log_data(ui.get_data())
    elif command == '2':
        bf.find_data()
    else:
        return


