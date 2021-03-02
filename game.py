
from utilities import validation,get_input
from chess import Board



board = Board()


response = get_input("Enter the knight's starting position")
if response:
    row, col = response
    board.move(row,col)
    print(board)











