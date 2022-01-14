from logging import raiseExceptions
from tracemalloc import stop


class Board:
    rows = 0
    columns = 0
    grid = []

    def __init__(self,rows,columns) -> None:
        self.rows = rows
        self.columns = columns
        self.reset()

    def reset(self):
        grid = []
        for _ in range(0,self.rows):
            row = []
            for _ in range(0,self.columns):
                row.append('-')
            grid.append(row)
        self.grid = grid

    def print(self):

        print(*range(self.columns))

        for row in self.grid:
            print(' '.join(row))

    def place_piece(self,column,piece) -> bool:
        stop_at = 5
        for index, row in enumerate(self.grid):
            if row[column] != '-':
                stop_at = index-1
                if stop_at < 0:
                    raise Exception('This row is full! Try again.')
                break
        
        self.grid[stop_at][column] = piece
      
        count = 1 #because current piece is player's piece
        row = stop_at 
        col = column 

        try:
            #
             #
              #
               #

            if self.grid[row-1][col-1] == piece:
                while self.grid[row-1][col-1] == piece:
                    count += 1
                    row-=1
                    col-=1
                    if count == 4:
                        return True
            row = stop_at
            col = column

            if self.grid[row+1][col+1] == piece:
                while self.grid[row+1][col+1] == piece:
                    count += 1
                    row+=1
                    col+=1
                    if count == 4:
                        return True
            row = stop_at
            col = column

        except:
            pass

        try:
            count = 1
               #
              #
             #
            #
            if self.grid[row-1][col+1] == piece:
                while self.grid[row-1][col+1] == piece:
                    count += 1
                    row-=1
                    col+=1
                    if count == 4:
                        return True
            row = stop_at
            col = column

            if self.grid[row+1][col-1] == piece:
                while self.grid[row+1][col-1] == piece:
                    count += 1
                    row+=1
                    col-=1
                    if count == 4:
                        return True
            row = stop_at
            col = column
        except:
            pass

        try:
            count = 1
            ####
            if self.grid[row][col+1] == piece:
                while self.grid[row][col+1] == piece:
                    count += 1
                    col+=1
                    if count == 4:
                        return True
            row = stop_at
            col = column

            if self.grid[row][col-1] == piece:
                while self.grid[row][col-1] == piece:
                    count += 1
                    col-=1
                    if count == 4:
                        return True
            row = stop_at
            col = column
        except:
            pass

        try:
            count = 1
            #
            #
            #
            #
            if self.grid[row+1][col] == piece:
                while self.grid[row+1][col] == piece:
                    count += 1
                    row+=1
                    if count == 4:
                        return True
            row = stop_at
            col = column

        except:
            pass

        return False