def check_win(board):
   win_combination = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_combination:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def draw_board(board):
    for i in range(3):
        print(board[0+i*3], "|", board[1+i*3], "|", board[2+i*3])
        print("-" * 9)

def in_simbol(player_token, board):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token + "? ")
      try:
         player_answer = int(player_answer)
      except:
         print("неправильный ввод")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("занято!")
      else:
        print("Введите число от 1 до 9")