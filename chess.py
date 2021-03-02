


class Board:
    empty = "__"

    def __init__(self, cols=8, rows=8):
        self.rows = rows
        self.cols = cols
        self.board = [ [Board.empty] * self.cols for i in range(self.rows)]


    def move(self,col,row,letter=" X"):
            self.board[row-1][col-1] = letter
    def valid_position(self, x,y):
        return   1 <= x <= self.cols and  1 <= y <=self.rows

    def find_position(self,col,row):
        positions = []

        for x in (2, -2):
            for y in (1, -1):
                if self.valid_position(col + x, row + y):
                    positions.append((col + x, row +y))
                if self.valid_position(col + y, row + x):
                    positions.append((col + y, row + x))

        return positions


    def __str__(self):
       size = len(self.board[0]) * 3 + 3
       heading = " " +  "-" * size
       board =heading + "\n"+\
       "\n".join( [ str(self.rows - i) + "| " + " ".join(row) + " |" for i,row in enumerate(self.board[::-1])])+"\n"+\
           heading+"\n"+\
         " " * 3 +  " ".join(list(map(lambda v : " " + str(v) ,range(1,self.cols + 1))))
       return board

