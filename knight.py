

from utilities import get_input,contains


class Game:
    
    def __init__(self, cols=8, rows=8):
        self.cols = cols
        self.rows = rows
        self.visited=[]
     
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
        return [(x, y, len(self.find_position(x, y)) - 1) for x,y in positions if self.is_empty(x,y)]
    
    def set_visited(self,col,row):
        self.visited.append((col,row))
        
    def is_empty(self,col,row):
        return not (col,row) in self.visited

    def is_explored(self,col, row):
        return  (col,row) in self.visited
    
    



    
class Board:

    empty = "__"
    visited =" *"

    def __init__(self, cols, rows):
        self.rows = rows
        self.cols = cols
        self.cells = [[Board.empty] * self.cols for i in range(self.rows)]

    def update(self,col,row,value=""):
        self.cells[row - 1][col - 1] = value or Board.visited

    def render(self, current_col, current_row, positions):

        self.cells[current_row - 1][current_col - 1] = " X"
        for col,row,v in positions:
            self.cells[row - 1][col -1] = " " + str(v)

        print(self)


        for col,row,v in positions:
            self.cells[row - 1][col -1] = Board.empty
        self.cells[current_row - 1][current_col - 1] = Board.visited



    def __str__(self):
        size = len(self.cells[0]) * 3 + 3
        heading = " " +  "-" * size
        cells =heading + "\n"+\
       "\n".join( [ str(self.rows - i) + "| " + " ".join(row) + " |" for i,row in enumerate(self.cells[::-1])])+"\n"+\
           heading+"\n"+\
         " " * 3 +  " ".join(list(map(lambda v : " " + str(v) ,range(1,self.cols + 1))))
        return cells



