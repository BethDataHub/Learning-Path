from Board import *

class Player:
    name = ''
    piece = ''
    wins = 0

    def __init__(self,name,piece) -> None:
        self.name = name
        self.piece = piece

    def take_turn(self,board:Board) -> bool:
        did_win = None
        while did_win == None:
            try:
                column = int(input(self.name+" enter your column choice: "))
                did_win = board.place_piece(column, self.piece)
            except Exception as err:
                print(err)
                pass
        return did_win
    
    def won(self):
        self.wins = self.wins+1
