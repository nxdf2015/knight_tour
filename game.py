
from utilities import get_input,contains
from chess import Board




n_cols,n_rows = get_input("Enter your board dimensions: ", "Invalid dimensions")

board = Board(n_cols,n_rows)

position = get_input("Enter the knight's starting position: ","Invalid positions", cols=n_cols, rows=n_rows)


col, row = position
length_tour = 0

while True:

    board.move(col, row)
    length_tour += 1
    positions = board.look_ahead(col,row)
    positions = [(* p,c) for * p,  c in positions  if board.isEmpty(* p )]
    if len(positions) == 0:
        if length_tour == board.cols * board.rows:
            print("What a great tour! Congratulations!")
        else:
           print("No more possible moves!")
           print(f"Your knight visited {length_tour} squares!")
        break


    for position in positions:
        board.move(position[0],position[1],str(position[2]))
    print(board)

    while True:
        next_position = get_input("Enter your next move: ","Invalid move!")
        if not board.is_explored(* next_position)  and contains(next_position,positions):
            for position in positions:

                board.move(position[0],position[1],"__")
            board.move(col,row,"*")
            col,row = next_position

            break
        else:
            print("Invalid move!", end=" ")
















