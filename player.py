
from utilities import contains, get_input
from knight import Game, Board

def play(col, row, n_cols, n_rows):
    length_tour = 0
    chess = Game(n_cols,n_rows)
    board = Board(n_cols, n_rows)
    while True:

        length_tour += 1
        chess.set_visited(col,row)

        positions = chess.look_ahead(col,row)
        if len(positions) == 0:
            if length_tour ==  n_cols * n_rows:
                print("What a great tour! Congratulations!")
            else:
               print("No more possible moves!")
               print(f"Your knight visited {length_tour} squares!")
            break

        board.update(col,row)
        board.render(col,row,positions)
        while True:
            next_position = get_input("Enter your next move: ","Invalid move!")
            if not chess.is_explored(* next_position)  and contains(next_position,positions):
                col,row = next_position
                break
            else:
                print("Invalid move!", end=" ")



if __name__ == "__main__":
    play(1,3,4,4)
