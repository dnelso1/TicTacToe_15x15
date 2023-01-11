# Description: The class Board represents the board for a two-player tic-tac-toe game, but
#              it's played on a 15x15 board and the goal is to get 5 in row.
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

class Board:
    """Represents the board for a tic-tac-toe game played on a 15x15 square grid"""
    def __init__(self):
        """Initializes the 15x15 board with spaces and the state of gameplay as UNFINISHED"""
        self._board = [[' ' for x in range(15)] for y in range(15)]
        self._current_state = "UNFINISHED"

    def get_current_state(self) -> str:
        """Returns the current state of the board"""
        return self._current_state

    def set_current_state(self, state) -> str:
        """Sets the current state of the board"""
        self._current_state = state

    def is_winner(self, row, col, player) -> bool:
        """Checks if a player has won by getting 5 in a row horizontally, vertically, or diagonally."""
        # checks for wins when the rows are between 0-10 and columns are between 0-10
        if row <= 10 and col <= 10:
            if self.is_vertical_win(row, col, player) or self.is_horizontal_win(row, col, player) or self.is_diagonal_win_decreasing(row, col, player) or self.is_diagonal_win_increasing(row, col, player):
                return True
        # checks for wins when the rows are between 11-14 and columns are between 0-10
        elif row >= 11 and col <= 10:
            if self.is_horizontal_win(row, col, player):
                return True
        # checks for wins when the rows are between 0-10 and columns are between 11-14
        elif row <= 10 and col >= 11:
            if self.is_vertical_win(row, col, player) or self.is_diagonal_win_increasing(row, col, player):
                return True
        # checks for wins when the rows are between 11-14 and columns are between 11-14
        elif row >= 11 and col >= 11:
            # checks for a vertical win
            if self.is_vertical_win(row, col, player) or self.is_horizontal_win(row, col, player):
                return True
        
        return False

    def is_draw(self) -> int:
        """Checks the conditions for a DRAW, which is when all squares are filled, but there is no winner. Returns the number of available moves remaining"""
        board = self._board
        available_moves = 0
        for row in range(len(board)):
            for col in range(len(board[row])):
                # checks every space for a space (' ') string;
                # if one is present and the game has not been won then available_moves is incremented by 1
                if board[row][col] == ' ' and (self._current_state != "X_WON" or self._current_state != "O_WON"):
                    available_moves += 1
        return available_moves

    def is_vertical_win(self, row, col, player) -> bool:
        """Checks for a vertical win. Returns True if a win exists, False otherwise"""
        board = self._board
        vertical_counting_up = board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and board[row + 3][col] == player and board[row + 4][col] == player
        vertical_counting_down = board[row][col] == player and board[row - 1][col] == player and board[row - 2][col] == player and board[row - 3][col] == player and board[row - 4][col] == player
        
        if vertical_counting_up or vertical_counting_down:
            return True
        
        return False

    def is_horizontal_win(self, row, col, player) -> bool:
        """Checks for a horizontal win. Returns True if a win exists, False otherwise"""
        board = self._board
        horizontal_counting_right = board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and board[row][col + 3] == player and board[row][col + 4] == player
        horizontal_counting_left = board[row][col] == player and board[row][col - 1] == player and board[row][col - 2] == player and board[row][col - 3] == player and board[row][col - 4] == player

        if horizontal_counting_right or horizontal_counting_left:
            return True
        
        return False

    def is_diagonal_win_decreasing(self, row, col, player) -> bool:
        """Checks for a diagonal win with a decreasing slope (such as \ ). Returns True if a win exists, False otherwise"""
        board = self._board
        return board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player and board[row + 4][col + 4] == player

    def is_diagonal_win_increasing(self, row, col, player) -> bool:
        """Checks for a diagonal win with a increasing slope (such as \ ). Returns True if a win exists, False otherwise"""
        board = self._board
        return board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][col - 2] == player and board[row + 3][col - 3] == player and board[row + 4][col - 4] == player

    def get_board(self) -> bool:
        """Returns the current board"""
        return self._board

    def print_board(self) -> None:
        """Prints the board to the screen"""
        print("\n\n\n\n")
        board = self._board
        horizontal_border = " ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---"
        for r in board:
            displayed_row = "|"
            for c in range(len(r)):
                #print(r[c]),
                displayed_row += f" {r[c]} |"
            print(horizontal_border)
            print(displayed_row)
        print(horizontal_border)
