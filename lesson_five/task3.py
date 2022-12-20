'''
Создайте программу для игры в "Крестики-нолики".
Вариант интерфейса:
 1  |  2 | 3
--------------
 4  |  5 | 6
--------------
7   | 8  | 9
'''


print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[ 0 + i * 3], "|", board[ 1 + i * 3], "|", board[ 2 + i * 3], "|")
      print("-" * 13)

def take_input(token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + token + "? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coor = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for e in win_coor:
       if board[e[0]] == board[e[1]] == board[e[2]]:
          return board[e[0]]
   return False

def main(board):
    count = 0
    win = False
    while not win:
        draw_board(board)
        if count % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        count += 1
        if count > 4:
           temp = check_win(board)
           if temp:
              print(temp, "выиграл!")
              win = True
              break
        if count == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

input("Нажмите Enter для выхода!")