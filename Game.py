from Board import Board

class Game:
    def make_move(self, row, col, player):
        """Makes a move based on the given [row][col] position and which player is making a turn, 'x' or 'o'"""
        board = Board.get_board()
        print(board)
        # returns False if there is a player occupying the [row][col] space or if the game has been won or drawn
        if board[row][col] == player or Board.get_current_sate() != "UNFINISHED":
            return False

        # records the player's move at the [row][col] space
        board[row][col] = player

        # if the current player has 5 in a row, the game state is updated to <player>_WON
        if Board.is_winner(row, col, player):
            Board.set_current_state(f"{player.upper()}_WON")
        # if there are no available moves left and neither player has won, the game state is changed to DRAW
        elif Board.is_draw() == 0:
            Board.set_current_state("DRAW")

        return True