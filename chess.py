from utilities import in_range

class Board:
    empty = "_"
    player = "X"
    def __init__(self, rows=8, cols=8):
        self.rows = rows
        self.cols = cols
        self.board = [ [Board.empty] * self.cols for i in range(self.rows)]


    def move(self,col,row):
        is_valid = in_range()
        if is_valid(row) and is_valid(col):
            self.board[row-1][col-1] = Board.player
        else:
            print("Invalid position!")


    def __str__(self):
       heading = " " +  "-" * 19
       board =heading + "\n"+\
       "\n".join( [ str(self.rows - i) + "| " + " ".join(row) + " |" for i,row in enumerate(self.board[::-1])])+"\n"+\
           heading+"\n"+\
         " " * 3 +  " ".join(list(map(str,range(1,9))))
       return board

