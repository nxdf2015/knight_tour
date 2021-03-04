
from knight import Game, Board
from operator import itemgetter

def play(col,row,n_cols, n_rows,game,visited=[]):



    visited = visited  + [(col,row)]

    positions = [(*p , v) for *p, v in  game.look_ahead(col,row) if not tuple(p) in visited]

    if len(positions) == 0:

        if len(visited) == n_rows * n_cols:
            return visited
        else:
            return False

    else:
        positions.sort(key=itemgetter(2),reverse=True)
        for next_col,next_row,v in positions:

            result = play(next_col, next_row, n_cols, n_rows,game,visited[:])

            if result:
                return result

        return False


