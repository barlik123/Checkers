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

#gets a board and two cordinates and updates orig_cord to empty
#(O) and dest_cord on the board to having a piece (X)
def update_piece(orig_cord: Tuple[int,int], dest_cord: Tuple[int,int],
                board: BOARD_TYPE):
    board[orig_cord[0]][orig_cord[1]] = 'O'
    board[dest_cord[0]][dest_cord[1]] = 'X'

#function that checks if a piece can move from cord1 to cord2
#on the board. (if there is a piece in the selected location
# and no piece in the destination location)
#the function returns a boolean.
def can_move(orig_cord: Tuple[int,int], dest_cord: Tuple[int,int],
                board: BOARD_TYPE) ->bool:
    return board[orig_cord[0]][orig_cord[1]]=='X' and board[dest_cord[0]][dest_cord[1]]=='O'

#function that executes the movement logic of the piece.
#gets the original and new cordinates and board,
#checks if the piece can move to the new cordinates
#and moves it there.
def move_piece(orig_cord: Tuple[int,int], dest_cord: Tuple[int,int],
                board: BOARD_TYPE) -> None:
    if can_move(orig_cord, dest_cord, Board1) and move_range(orig_cord, dest_cord):
        update_piece(orig_cord, dest_cord, Board1)

#function that checks if the destination cordinates of a move
#are withing one diagonal square from the origin cordinate
#and returns a boolean 
def move_range(orig_cord: Tuple[int,int], dest_cord: Tuple[int,int]) -> bool:
    return (dest_cord[0] == orig_cord[0] - 1 and 
        (dest_cord[1] == orig_cord[1] + 1 or dest_cord[1] == orig_cord[1] -1))
        
move_piece((5,1),(4,0),Board1)
move_piece((5,5),(4,6),Board1)
move_piece((4,0),(3,1),Board1)
print('\n')
print_board(Board1)