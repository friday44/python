import ui
import book_save as bs
import book_find as bf

def button_click():
    operation = ui.get_comand()
    if operation == '1':
        bs.log_data(ui.get_data())
    elif operation == '2':
        ui.print_data(bf.find_data(ui.get_find_string()))
  

def button_click():
    operation = 0
    while operation != '4':
        operation = ui.get_comand()
        if operation == '1':
            bs.log_data(ui.get_data())
            operation = ui.get_comand()
        elif operation == '2':
            ui.print_data(bf.find_data(ui.get_find_string()))
            operation = ui.get_comand()
        else:
            operation = '4'