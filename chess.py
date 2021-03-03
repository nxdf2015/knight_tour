



class Board:
    empty = "__"

    def __init__(self, cols=8, rows=8):
        self.rows = rows
        self.cols = cols
        self.board = [[Board.empty] * self.cols for i in range(self.rows)]
        self.route = []


    def move(self,col,row,letter="X"):
            self.board[row-1][col-1] = letter.rjust(2," ")

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

    def look_ahead(self,col,row):

        positions = [ p for p in self.find_position(col,row) if not p == (col,row)]
        return [ (x, y, len(self.find_position(x, y)) - 1) for x,y in positions]


    def isEmpty(self,col, row):
        return not self.board[row - 1][col - 1] == " *"

    def is_explored(self,col,row):
        return self.board[row -1 ][col - 1] in "X*"

    def __str__(self):
       size = len(self.board[0]) * 3 + 3
       heading = " " +  "-" * size
       board =heading + "\n"+\
       "\n".join( [ str(self.rows - i) + "| " + " ".join(row) + " |" for i,row in enumerate(self.board[::-1])])+"\n"+\
           heading+"\n"+\
         " " * 3 +  " ".join(list(map(lambda v : " " + str(v) ,range(1,self.cols + 1))))
       return board

