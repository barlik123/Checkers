from typing import Callable, Dict, List, Any, Tuple

BOARD_LENGTH = 8
BOARD_TYPE = List[List[int]]

#initializes a Board layout
def init_board() ->BOARD_TYPE:
    Board = [['X' if (j+i)%2==0 and (j<3 or j>4) else 'O' for i in range(BOARD_LENGTH)] for j in range(BOARD_LENGTH) ]
    return Board


#gets a board input and prints the Board 
def print_board(board: BOARD_TYPE) ->None:
    for i in range(BOARD_LENGTH):
        for j in range (BOARD_LENGTH):
            print(board[i][j], end=' ')
        print()

#gets a board and two cordinates and updates orig_cord to empty box
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
    if can_move(orig_cord, dest_cord, board) and move_range(orig_cord, dest_cord):
        update_piece(orig_cord, dest_cord, board)

#function that checks if the destination cordinates of a move
#are withing one diagonal square from the origin cordinate
#and returns a boolean 
def move_range(orig_cord: Tuple[int,int], dest_cord: Tuple[int,int]) -> bool:
    return (dest_cord[0] == orig_cord[0] - 1 and 
        (dest_cord[1] == orig_cord[1] + 1 or dest_cord[1] == orig_cord[1] -1))


def game() -> None:
    Board1 = init_board()
    print_board(Board1)
    Keep_playing = True
    while (Keep_playing):
        x1 , y1, x2, y2 = input("please input the coordinates for before and after the move in this format x1,y1,x2,y2: ").split(',')
        move_piece((int(x1),int(y1)),(int(x2),int(y2)),Board1)
        print_board(Board1)
        finish_playing = input("Do you want to stop playing? \nY/N: ")
        if (finish_playing == "Y"):
            Keep_playing = False
        
game()    
#move_piece((5,1),(4,0),Board1)
#move_piece((5,5),(4,6),Board1)
#move_piece((4,0),(3,1),Board1)
#print('\n')
