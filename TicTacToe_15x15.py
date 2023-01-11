# Author: Andrew Nelson
# Date: 06/04/2020
# Description: A class called FiveBoard represents the board for a two-player tic-tac-toe game, but
#              instead it's played on a 15x15 board and the goal is to get 5 in row.
#
#              Players can move their pieces using the make_move function, which takes either an 'x' or 'o',
#              depending on which player is making the move and the row/column position on the board where the 'x'/'o'
#              will be placed.

'''
Write a class called FiveBoard that represents the board for a two-player game that is like [tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe), 
but on a larger scale.  Instead of a 3x3 board, it is played on a 15x15 board, and instead of 3 in a row, each player is trying to get 5 in row.

The class should have two **private** data members - a list of lists that represents the board, and the current state, which holds one of 
the four following values: "X_WON", "O_WON", "DRAW", or "UNFINISHED".  It should have a get method named get_current_state, which returns the current state.

The class should have an init method that initializes the board to a list of 15 lists that each contain 15 empty strings (where each 
represents an empty square), and initializes the current_state to "UNFINISHED".

It should have a method named make_move that takes three parameters, a row and a column (in that order) where each is an integer in the 
range 0-14, and either 'x' or 'o' to indicate the player who is making the move. If that square is already occupied, or if the game has 
already been won or drawn, make_move should return False. Otherwise, it should record the move, update the current_state, and return True. 
**It's possible for multiple moves to be made in a row for the same player (so you don't need to enforce alternating turns).** 
A game is drawn when all of the squares are filled, but neither player has won.

It's not required, but you'll probably find it useful for testing and debugging to have a method that prints out the board.

Whether you think of the array indices as being [row][column] or [column][row] doesn't matter as long as you're consistent.

Your class only represents the board, it doesn't actually allow two players to play the game.  Other code (that you don't have to write) 
would use your FiveBoard class to make that happen.

For example, your class could be used as follows:
board = FiveBoard()
board.make_move(0, 0, 'o')
board.make_move(6, 5, 'x')
board.make_move(2, 1, 'x')
board.make_move(3, 2, 'x')
board.get_current_state()
'''

class FiveBoard:
    """Represents the board for a tic-tac-toe game played on a 15x15 square grid"""
    def __init__(self):
        """Initializes the 15x15 board with empty strings and the state of gameplay as UNFINISHED"""
        self._board = [
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        ]
        self._current_state = "UNFINISHED"

    def get_current_state(self):
        """Returns the current state of the board"""
        return self._current_state

    def make_move(self, row, column, player):
        """Makes a move based on the given [row][column] position and which player is making a turn, 'x' or 'o'"""
        board = self._board
        for r in board:
            print(r)
        # returns False if there is a player occupying the [row][column] space or if the game has been won or drawn
        if board[row][column] == 'x' or board[row][column] == 'o' or self._current_state != "UNFINISHED":
            return False
        else:
            # records the player's move at the [row][column] space
            board[row][column] = player
            # if 'x' has 5 in a row, the game state is updated to X_WON
            if self.is_x_won():
                self._current_state = "X_WON"
            # if 'o' has 5 in a row, the game state is updated to O_WON
            elif self.is_o_won():
                self._current_state = "O_WON"
            # if there are no available moves left and neither player has won, the game state is changed to DRAW
            elif self.is_draw() == 0:
                self._current_state = "DRAW"
            return True

    def is_x_won(self):
        """Checks if 'x' has won by getting 5 in a row horizontally, vertically, or diagonally."""
        board = self._board
        for row in range(len(board)):
            for column in range(len(board[row])):
                # checks for wins when the rows are between 0-10 and columns are between 0-10
                if row <= 10 and column <= 10:
                    # checks for a vertical win
                    if board[row][column] == 'x' and board[row + 1][column] == 'x' and board[row + 2][column] == 'x' and board[row + 3][column] == 'x' and board[row + 4][column] == 'x':
                        self._current_state = "X_WON"
                    # checks for a horizontal win
                    if board[row][column] == 'x' and board[row][column + 1] == 'x' and board[row][column + 2] == 'x' and board[row][column + 3] == 'x' and board[row][column + 4] == 'x':
                        self._current_state = "X_WON"
                    # checks for a diagonal win with a decreasing slope (such as \ )
                    elif board[row][column] == 'x' and board[row + 1][column + 1] == 'x' and board[row + 2][column + 2] == 'x' and board[row + 3][column + 3] == 'x' and board[row + 4][column + 4] == 'x':
                        self._current_state = "X_WON"
                    # checks for a diagonal win with an increasing slope (such as / )
                    elif board[row][column] == 'x' and board[row + 1][column - 1] == 'x' and board[row + 2][column - 2] == 'x' and board[row + 3][column - 3] == 'x' and board[row + 4][column - 4] == 'x':
                        self._current_state = "X_WON"
                # checks for wins when the rows are between 11-14 and columns are between 0-10
                elif row >= 11 and column <= 10:
                    # checks for a horizontal win
                    if board[row][column] == 'x' and board[row][column + 1] == 'x' and board[row][column + 2] == 'x' and board[row][column + 3] == 'x' and board[row][column + 4] == 'x':
                        self._current_state = "X_WON"
                # checks for wins when the rows are between 0-10 and columns are between 11-14
                elif row <= 10 and column >= 11:
                    # checks for a vertical win
                    if board[row][column] == 'x' and board[row + 1][column] == 'x' and board[row + 2][column] == 'x' and board[row + 3][column] == 'x' and board[row + 4][column] == 'x':
                        self._current_state = "X_WON"
                    # checks for a diagonal win with an increasing slope (such as / )
                    elif board[row][column] == 'x' and board[row + 1][column - 1] == 'x' and board[row + 2][column - 2] == 'x' and board[row + 3][column - 3] == 'x' and board[row + 4][column - 4] == 'x':
                        self._current_state = "X_WON"
                # checks for wins when the rows are between 11-14 and columns are between 11-14
                elif row >= 11 and column >= 11:
                    # checks for a vertical win
                    if board[row][column] == 'x' and board[row - 1][column] == 'x' and board[row - 2][column] == 'x' and board[row - 3][column] == 'x' and board[row - 4][column] == 'x':
                        self._current_state = "X_WON"
                    # checks for a horizontal win
                    elif board[row][column] == 'x' and board[row][column - 1] == 'x' and board[row][column - 2] == 'x' and board[row][column - 3] == 'x' and board[row][column - 4] == 'x':
                        self._current_state = "X_WON"

    def is_o_won(self):
        """Checks if 'o' has won by getting 5 in a row horizontally, vertically, or diagonally."""
        board = self._board
        for row in range(len(board)):
            for column in range(len(board[row])):
                # checks for wins when the rows are between 0-10 and columns are between 0-10
                if row <= 10 and column <= 10:
                    # checks for a vertical win
                    if board[row][column] == 'o' and board[row + 1][column] == 'o' and board[row + 2][column] == 'o' and board[row + 3][column] == 'o' and board[row + 4][column] == 'o':
                        self._current_state = "O_WON"
                    # checks for a horizontal win
                    if board[row][column] == 'o' and board[row][column + 1] == 'o' and board[row][column + 2] == 'o' and board[row][column + 3] == 'o' and board[row][column + 4] == 'o':
                        self._current_state = "O_WON"
                    # checks for a diagonal win with a decreasing slope (such as \ )
                    elif board[row][column] == 'o' and board[row + 1][column + 1] == 'o' and board[row + 2][column + 2] == 'o' and board[row + 3][column + 3] == 'o' and board[row + 4][column + 4] == 'o':
                        self._current_state = "O_WON"
                    # checks for a diagonal win with a increasing slope (such as / )
                    elif board[row][column] == 'o' and board[row + 1][column - 1] == 'o' and board[row + 2][column - 2] == 'o' and board[row + 3][column - 3] == 'o' and board[row + 4][column - 4] == 'o':
                        self._current_state = "O_WON"
                # checks for wins when the rows are between 11-14 and columns are between 0-10
                elif row >= 11 and column <= 10:
                    # checks for a horizontal win
                    if board[row][column] == 'o' and board[row][column + 1] == 'o' and board[row][column + 2] == 'o' and board[row][column + 3] == 'o' and board[row][column + 4] == 'o':
                        self._current_state = "O_WON"
                # checks for wins when the rows are between 0-10 and columns are between 11-14
                elif row <= 10 and column >= 11:
                    # checks for a vertical win
                    if board[row][column] == 'o' and board[row + 1][column] == 'o' and board[row + 2][column] == 'o' and board[row + 3][column] == 'o' and board[row + 4][column] == 'o':
                        self._current_state = "O_WON"
                    # checks for a diagonal win with an increasing slope (such as / )
                    elif board[row][column] == 'o' and board[row + 1][column - 1] == 'o' and board[row + 2][column - 2] == 'o' and board[row + 3][column - 3] == 'o' and board[row + 4][column - 4] == 'o':
                        self._current_state = "O_WON"
                # checks for wins when the rows are between 11-14 and columns are between 11-14
                elif row >= 11 and column >= 11:
                    # checks for a vertical win
                    if board[row][column] == 'o' and board[row - 1][column] == 'o' and board[row - 2][column] == 'o' and board[row - 3][column] == 'o' and board[row - 4][column] == 'o':
                        self._current_state = "O_WON"
                    # checks for a horizontal win
                    elif board[row][column] == 'o' and board[row][column - 1] == 'o' and board[row][column - 2] == 'o' and board[row][column - 3] == 'o' and board[row][column - 4] == 'o':
                        self._current_state = "O_WON"

    def is_draw(self):
        """Checks the conditions for a DRAW. Returns the number of available moves remaining"""
        board = self._board
        available_moves = 0
        for row in range(len(board)):
            for column in range(len(board[row])):
                # checks every space for an empty string;
                # if one is present and the game has not been won then available_moves is incremented by 1
                if board[row][column] == ' ' and (self._current_state != "X_WON" or self._current_state != "O_WON"):
                    available_moves += 1
        return available_moves

if __name__ == '__main__':
    board = FiveBoard()
    board.make_move(0, 0, 'o')
    board.make_move(6, 5, 'x')
    board.make_move(2, 1, 'x')
    board.make_move(3, 2, 'x')
    print(board.get_current_state())