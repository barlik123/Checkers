from typing import Callable, Dict, List, Any, Tuple

BOARD_LENGTH = 8
BOARD_TYPE = List[List[int]]
COORDS_TYPE = Tuple[int,int] #the tuple is in format (row,column)

#initializes a Board layout
def init_board() ->BOARD_TYPE:
    #Board = [['X' if (j+i)%2==0 and (j<3 or j>4) else 'O' for i in range(BOARD_LENGTH)] for j in range(BOARD_LENGTH) ]
    board = []
    for i in range(8):
        row = []
        for j in range(8):
            if (i + j) % 2 != 0:
                if i < 3:
                    row.append("B")  # Black pieces
                elif i > 4:
                    row.append("W")  # White pieces
                else:
                    row.append("O")  # Empty squares
            else:
                row.append("O")  # Empty squares
        board.append(row)
    return board


#gets a board input and prints the Board 
def print_board(board: BOARD_TYPE) ->None:
    for i in range(BOARD_LENGTH):
        for j in range (BOARD_LENGTH):
            print(board[i][j], end=' ')
        print()

#gets a board and two cordinates and updates orig_cord to empty box
#(O) and dest_cord on the board to having a piece (X)
def update_piece(orig_cord: COORDS_TYPE, dest_cord: COORDS_TYPE,
                board: BOARD_TYPE, player: str):
    board[orig_cord[0]][orig_cord[1]] = 'O'
    board[dest_cord[0]][dest_cord[1]] = player

#function that checks if a piece can move from cord1 to cord2
#on the board. (if there is a piece in the selected location 
# and no piece in the destination location)
#the function returns a boolean.
def is_can_move(orig_cord: COORDS_TYPE, dest_cord: COORDS_TYPE,
                board: BOARD_TYPE, player: str) ->bool:
    return board[orig_cord[0]][orig_cord[1]]==player and board[dest_cord[0]][dest_cord[1]]=='O'

##############################MOVE PIECE FUNCTIONALITIES############################################

#function that checks if the destination cordinates of a move
#are withing one diagonal square from the origin cordinate
#and returns a boolean 
def move_range(orig_cord: COORDS_TYPE, dest_cord: COORDS_TYPE, player: str) -> bool:
    if player == "W":
        return (dest_cord[0] == orig_cord[0] - 1 and 
            (dest_cord[1] == orig_cord[1] + 1 or dest_cord[1] == orig_cord[1] -1))
    elif player == "B":
        return (dest_cord[0] == orig_cord[0] + 1 and 
            (dest_cord[1] == orig_cord[1] + 1 or dest_cord[1] == orig_cord[1] -1))


##############################EAT PIECE FUNCTIONALITIES############################################

def is_eatable(orig_cord: COORDS_TYPE, dest_cord: COORDS_TYPE, board: BOARD_TYPE, avg_row: int, avg_col: int, player: str) -> bool:
    if player == 'W':
        return ((dest_cord[0] == orig_cord[0] - 2) and (dest_cord[1] == orig_cord[1] + 2 or dest_cord[1] == orig_cord[1] - 2)) \
            and (board[avg_row][avg_col]=='B')
    elif player == 'B':
        return ((dest_cord[0] == orig_cord[0] + 2) and (dest_cord[1] == orig_cord[1] + 2 or dest_cord[1] == orig_cord[1] - 2)) \
            and (board[avg_row][avg_col]=='W')


def eat_piece(orig_cord: COORDS_TYPE, dest_cord: COORDS_TYPE,
                board: BOARD_TYPE, avg_row: int, avg_col: int, player: str) -> None:
    update_piece(orig_cord, dest_cord, board, player) #piece moved to new box
    board[avg_row][avg_col] = 'O' #ated piece

def single_play(orig_cord: COORDS_TYPE, dest_cord: COORDS_TYPE,
                board: BOARD_TYPE, player: str) -> None:
    avg_row = int((orig_cord[0] + dest_cord[0]) / 2)
    avg_col = int((orig_cord[1] + dest_cord[1]) / 2)
    if is_can_move(orig_cord, dest_cord, board, player) and is_eatable(orig_cord, dest_cord, board, avg_row, avg_col, player): #checks if the move is a eat move
        eat_piece(orig_cord,dest_cord,board,avg_row,avg_col, player)
    elif is_can_move(orig_cord, dest_cord, board, player) and move_range(orig_cord, dest_cord, player): #checks if the move is a simple move
        update_piece(orig_cord, dest_cord, board,player)


def game() -> None:
    board1 = init_board()
    print_board(board1) 
    player = 'W' #The player rotates between W (white) and B (black)
    Keep_playing = True
    while (Keep_playing):
        print("player turn: %s" %player)
        x1 , y1, x2, y2 = input("please input the coordinates for before and after the move in this format x1,y1,x2,y2: ").split(',')
        single_play((int(x1),int(y1)),(int(x2),int(y2)),board1, player)
        print_board(board1)
        finish_playing = input("Do you want to stop playing? \nY/N: ")
        if (finish_playing == "Y"):
            Keep_playing = False
        if player == 'B':
            player = 'W'
        elif player == 'W':
            player = 'B'
        
game()    

