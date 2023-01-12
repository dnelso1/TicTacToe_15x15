from Board import Board, board_inst

class Game:
    def __init__(self) -> None:
        self._player1 = ''
        self._player2  = ''

    def set_player1(self, icon)  -> None:
        self._player1 = icon

    def set_player2(self, icon) -> None:
        self._player2 = icon

    def get_player1(self) -> str:
        return self._player1

    def get_player2(self) -> str:
        return self._player2

    def make_move(self, row, col, player) -> bool:
        """Makes a move based on the given [row][col] position and which player is making a turn, 'x' or 'o'"""
        board = board_inst.get_board()
        
        # returns False if there is a player occupying the [row][col] space or if the game has been won or drawn
        if board[row][col] == player or board_inst.get_current_state() != "UNFINISHED":
            return False

        # records the player's move at the [row][col] space
        board[row][col] = player
        # if the current player has 5 in a row, the game state is updated to <player>_WON
        if board_inst.is_winner(player):
            board_inst.set_current_state(f"{player.upper()}_WON")
        # if there are no available moves left and neither player has won, the game state is changed to DRAW
        elif board_inst.is_draw() == 0:
            board_inst.set_current_state("DRAW")

        return True
