
from utilities import get_input
from chess import Board




n_cols,n_rows = get_input("Enter your board dimensions: ", "Invalid dimensions")

board = Board(n_cols,n_rows)

position = get_input("Enter the knight's starting position: ","Invalid positions", cols=n_cols, rows=n_rows)


col, row = position

board.move(col,row)

board.look_ahead(col,row)










