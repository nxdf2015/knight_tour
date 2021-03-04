
from utilities import get_input,contains
from knight import Board, Game

import player
import computer


# n_cols,n_rows = get_input("Enter your board dimensions: ", "Invalid dimensions")
#
# board = Board(n_cols,n_rows)
#
# position = get_input("Enter the knight's starting position: ","Invalid positions", cols=n_cols, rows=n_rows)
#
#
# col, row = position
# length_tour = 0
#
# while True:
#
#     board.move(col, row)
#     length_tour += 1
#     positions = board.look_ahead(col,row)
#     positions = [(* p,c) for * p,  c in positions  if board.isEmpty(* p )]
#     if len(positions) == 0:
#         if length_tour == board.cols * board.rows:
#             print("What a great tour! Congratulations!")
#         else:
#            print("No more possible moves!")
#            print(f"Your knight visited {length_tour} squares!")
#         break
#
#
#     for position in positions:
#         board.move(position[0],position[1],str(position[2]))
#     print(board)
#
#     while True:
#         next_position = get_input("Enter your next move: ","Invalid move!")
#         if not board.is_explored(* next_position)  and contains(next_position,positions):
#             for position in positions:
#
#                 board.move(position[0],position[1],"__")
#             board.move(col,row,"*")
#             col,row = next_position
#
#             break
#         else:
#             print("Invalid move!", end=" ")
#
#
#
#
#
#
#
#
#



n_cols,n_rows = get_input("Enter your board dimensions: ", "Invalid dimensions")



position = get_input("Enter the knight's starting position: ","Invalid positions", cols=n_cols, rows=n_rows)


col, row = position
length_tour = 0
choice = " "
while True:
    choice = input("Do you want to try the puzzle?(y/n) ")
    if choice == "y" or choice == "n":
        break
    print("Invalid choice")

if choice ==  "y":
    if n_rows < 4 and n_cols < 4:
        print("No solution exists!")
    else:
        player.play(col, row, n_cols, n_rows)
else:

    game = Game(n_cols, n_rows)
    positions = computer.play(col, row, n_cols, n_rows, game)
    if positions:
        print("Here 's the solution!")
        board = Board(n_cols, n_rows)
        for i, p in enumerate(positions,1):
            col,row = p
            board.update(col,row,  str(i).rjust(2," "))
        print(board)
    else:
        print("No solution exists!")



