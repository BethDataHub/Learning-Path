from Player import *
from Board import *
import random

def leaderboard(player_one,player_two):
    name_len = max(len(player_one.name), len(player_two.name))
    wins_len = max(len(str(player_one.wins)),len(str(player_two.wins)))
    print("-" * (7+name_len+wins_len))
    print(player_one.name,'wins:',player_one.wins)
    print(player_two.name,'wins:',player_two.wins)
    print("-" * (7+name_len+wins_len))

def main():
    player_one_name = input("Player one, enter your name: ")
    player_one_piece = (input("Player one, choose your piece: ") or 'O')
    player_two_name = input("Player two, enter your name: ")
    player_two_piece = (input("Player two, choose your piece: ") or 'X')

    player_one = Player(player_one_name,player_one_piece)
    player_two = Player(player_two_name,player_two_piece)
    board = Board(6,7)
    players = [player_one,player_two]

    still_playing = True
    while still_playing == True:
        players_turn = random.choice([0,1])
        game_over = False
        winner = None
        while game_over == False:
            board.print()
            did_win = players[players_turn].take_turn(board)
            if did_win == True:
                winner = players[players_turn]
                game_over = True
            else: 
                players_turn = players_turn+1
                players_turn = players_turn%2

        board.print()
        winner.won()
        print(winner.name+' won!')
        leaderboard(player_one,player_two)
        if input('Keep playing?(Y/n) ').upper() == 'N':
            still_playing = False
        else:
            board.reset()

if __name__ == '__main__':
    main()