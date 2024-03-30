from typing import Callable, Dict, List, Any, Tuple

BOARD_LENGTH = 8
BOARD_TYPE = List[List[int]]

#initializes a Board layout
def init_board() ->BOARD_TYPE:
    Board = [['X' if (j+i)%2==0 and (j<3 or j>4) else 'O' for i in range(BOARD_LENGTH)] for j in range(BOARD_LENGTH) ]
    return Board

Board1 = init_board()

#gets a board input and prints the Board 
def print_board(board: BOARD_TYPE) ->None:
    for i in range(BOARD_LENGTH):
        for j in range (BOARD_LENGTH):
            print(Board1[i][j], end=' ')
        print()

print_board(Board1)

#gets a board and two cordinates and updates cord1 to empty
#(O) and cord2 on the board to having a piece (X)
def update_piece(cord1: Tuple[int,int], cord2: Tuple[int,int],
                board: BOARD_TYPE):
    board[cord1[0]][cord1[1]] = 'O'
    board[cord2[0]][cord2[1]] = 'X'

#function that checks if a piece can move from cord1 to cord2
#on the board. 
#the function returns a boolean.
def can_move(cord1: Tuple[int,int], cord2: Tuple[int,int],
                board: BOARD_TYPE) ->bool:
    return board[cord1[0]][cord1[1]]=='X' and board[cord2[0]][cord2[1]]=='O'

#function that executes the movement logic of the piece.
#gets the original and new cordinates and board,
#checks if the piece can move to the new cordinates
#and moves it there.
def move_piece(cord1: Tuple[int,int], cord2: Tuple[int,int],
                board: BOARD_TYPE) -> None:
    if can_move(cord1, cord2, Board1):
        update_piece(cord1, cord2, Board1)

move_piece((3,3),(5,6),Board1)
move_piece((1,7),(2,2),Board1)
print('\n')
print_board(Board1)