# "Крестики-нолики".
import functions as f


print('\n', 'Крестики-нолики', '\n')
board = list(range(1,10))
count = 0
win = False
while not win:
    f.draw_board(board)
    if count % 2 == 0:
        f.in_simbol("X", board)
    else:
        f.in_simbol("O", board)
    count += 1
    if count > 4:
        temp = f.check_win(board)
        if temp:
            print(temp, "выиграл!")
            win = True
            break
    if count == 9:
        print("Ничья!")
        break
f.draw_board(board)
