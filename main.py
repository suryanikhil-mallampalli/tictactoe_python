# M.P.1
import random
def display_board(board):
  print('   |   |')
  print(' '+board[7]+' | '+board[8]+' | '+board[9])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' '+board[4]+' | '+board[5]+' | '+board[6])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' '+board[1]+' | '+board[2]+' | '+board[3])
  print('   |   |')


def player_input():
  marker=''
  while not(marker == 'X' or marker=='O'):
    marker=input('Player 1: Do you want it to be X or O?')
  if marker=='X':
    return ('X','O')
  else:
    return ('O','X')


def place_marker(board,marker,position):
  board[position]=marker


def winner_check(board,marker):
  return((board[9]==marker and board[8]==marker and board[7]==marker) or
         (board[6]==marker and board[5]==marker and board[4]==marker) or
         (board[3]==marker and board[2]==marker and board[1]==marker) or
         (board[7]==marker and board[4]==marker and board[1]==marker) or
         (board[8]==marker and board[5]==marker and board[2]==marker) or
         (board[9]==marker and board[6]==marker and board[3]==marker) or
         (board[1]==marker and board[5]==marker and board[9]==marker) or
         (board[7]==marker and board[5]==marker and board[3]==marker))
    

def start_player():
  if random.randint(0,1)=='0':
    return 'player2'
  else:
    return 'player1'


def space_check(board,position):
  return board[position]==' '


def full_check(board):
  return not (' ' in board)


def next_position(board,):
  position=0
  while (position not in [1,2,3,4,5,6,7,8,9] or space_check(board,position)):
    position = int(input('Choose your next position(1-9): '))
    break
  return position


def replay():
  return input('Do you want to play again? Enter Yes or No: ')


#simulator code
print('Welcome to TIC-TAC-TOE !!')
while True:
  #clearing the board each time
  theBoard=[' ']*10
  game_on=True
  player1_marker,player2_marker=player_input()
  turn=start_player()
  print(turn+', Will go first.')
  play_game=input('Are you ready to play? Y or N: ')
  if play_game.lower()=='y':
    game_on=True
  else:
    game_on= False
  while game_on:
    print('The initial board was set as follows: ')
#chance of player1
    if turn=='player1':
      display_board(theBoard)
      position=next_position(theBoard)
      place_marker(theBoard,player1_marker,position)
      if winner_check(theBoard, player1_marker):
        display_board(theBoard)
        print('Congratulations, Player 1, has won the game')
        game_on=False
      else:
        if full_check(theBoard):
          print('Hey its a Draw match! ')
          game_on=False
        else:
          turn='player2'
#chance of player2
    else:
      display_board(theBoard)
      position=next_position(theBoard)
      place_marker(theBoard,player2_marker,position)
      if winner_check(theBoard, player2_marker):
        display_board(theBoard)
        print('Congratulations, Player 2, has won the game')
        game_on=False
      else:
         if full_check(theBoard):
          print('Hey its a Draw match! ')
          game_on=False
         else:
          turn='player1'
  if not replay():
    break