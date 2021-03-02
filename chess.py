

class Board:
    empty = "__"
    player = " X"
    def __init__(self, cols=8, rows=8):
        self.rows = rows
        self.cols = cols
        self.board = [ [Board.empty] * self.cols for i in range(self.rows)]


    def move(self,col,row):
            self.board[row-1][col-1] = Board.player



    def __str__(self):
       size = len(self.board[0]) * 3 + 3
       heading = " " +  "-" * size
       board =heading + "\n"+\
       "\n".join( [ str(self.rows - i) + "| " + " ".join(row) + " |" for i,row in enumerate(self.board[::-1])])+"\n"+\
           heading+"\n"+\
         " " * 3 +  " ".join(list(map(lambda v : " " + str(v) ,range(1,self.cols + 1))))
       return board

