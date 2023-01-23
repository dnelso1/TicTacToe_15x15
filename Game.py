from Board import Board, board_inst
from os import system
from time import sleep

class Game:
    def make_move(self, row, col, player) -> None:
        """Makes a move based on the given [row][col] position and which player is making a turn, 'x' or 'o'"""
        board = board_inst.get_board()
        
        # returns False if there is a player occupying the [row][col] space or if the game has been won or drawn
        if board[row][col] != " ":
            print("That space is not open! Try again.")
            sleep(1.5)

        # records the player's move at the [row][col] space
        board[row][col] = player
        # if the current player has 5 in a row, the game state is updated to <player>_WON
        if board_inst.is_winner(player):
            board_inst.set_current_state(f"{player.upper()}_WON")
        # if there are no available moves left and neither player has won, the game state is changed to DRAW
        elif board_inst.is_draw() == 0:
            board_inst.set_current_state("DRAW")
    
    def play_game(self) -> None:
        """Plays the game until it is finished"""
        while board_inst.get_current_state() == 'UNFINISHED':
            system('clear')
            board_inst.print_board()
            player = input("Who is making a move? (x/o) > ")
            system('clear')
            board_inst.print_board()
            move = input(f"What is {player.upper()}'s move? (Enter a row,column coordinate: 1,4) > ")
            move = tuple(move.split(","))
            self.make_move(int(move[0]), int(move[1]), player.lower())
        
        system('clear')
        if board_inst.get_current_state() == 'X_WON':
            print("X Wins!!!")
        elif board_inst.get_current_state() == 'O_WON':
            print("O Wins!!!")
        elif board_inst.get_current_state() == 'DRAW':
            print("Sadly, it was a DRAW")
        sleep(5)
        system('clear')
