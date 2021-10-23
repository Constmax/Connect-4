"""
stores all the information
"""


class Game:
    def __init__(self):
        self.board = [
            ["--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "Rc", "--", "Rc", "--", "--"],
            ["--", "--", "--", "Rc", "--", "--", "--"],
            ["--", "--", "RC", "--", "RC", "--", "--"],
            ["--", "Rc", "--", "--", "--", "RC", "--"],
            ["--", "--", "--", "--", "--", "--", "Rc"]
        ]
        self.red_to_move = True
        self.move_col = []
        self.available_cols = []

    # makes move in board and switches move indicator
    def make_move(self, move):

        if self.board[0][move[0]] == "--" and self.red_to_move:
            print("here")
            self.board[0][move[0]] = "Rc"

        elif self.board[0][move[0]] == "--":
            self.board[0][move[0]] = "Yc"

        self.red_to_move = not self.red_to_move

    """
    makes the chips drop to their position
    """

    def makes_chips_drop(self):
        for r in range(0, 1):  # iterates through the board
            for c in range(0, 7):
                chip = self.board[r][c]  # chip is the current board position assigned
                if chip != "--":  # checks if chip is a chip or just empty
                    counter = 1
                    for j in range(0, 5):
                        if self.board[r + counter][c] == "--":
                            self.board[r + counter][c] = chip  # drops chip one row down
                            self.board[r + counter - 1][c] = "--"  # empties the row above the chip
                        counter = counter + 1

    def check_for_win(self):
        self.horizontal_win()
        self.vertical_win()
        self.diagonal_win()

    def horizontal_win(self):  # needs still a lot of work change counters
        for r in range(0, 6):
            for c in range(0, 7):
                chip = self.board[r][c]
                if chip != "--":
                    win_counter = 0
                    for i in range(0, 4):  # checks the squares underneath the selected chip
                        if c - i < 0:
                            break
                        elif chip == self.board[r][c - i]:
                            win_counter = win_counter + 1

                        if win_counter == 4:  # tells you when you win and resets the playing board
                            print("You won")
                            win_counter = 1
                            return True

    def vertical_win(self):
        for r in range(0, 6):
            for c in range(0, 7):
                chip = self.board[r][c]
                if chip != "--":
                    win_counter = 0
                    for i in range(0, 4):  # checks the squares underneath the selected chip
                        if r - i < 0:
                            break
                        elif chip == self.board[r - i][c]:
                            win_counter += 1

                        if win_counter == 4:  # tells you when you win and resets the playing board
                            print("You won")
                            win_counter = 1
                            return True

    def diagonal_win(self):
        for r in range(0, 6):
            for c in range(0, 7):
                chip = self.board[r][c]
                if chip != "--":
                    win_counter = 0
                    for i in range(0, 4):
                        if r + i > 5 or c + i > 6:
                            break
                        elif chip == self.board[r + i][c + i]:
                            win_counter += 1

                    if win_counter == 4:
                        print("you won")
                        self.board = [
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"]
                        ]
                        win_counter = 0
                        return True
                    else:
                        win_counter = 0

                    for i in range(0, 4):
                        if r - i < 0 or c + i > 6:
                            break
                        elif chip == self.board[r - i][c + i]:
                            win_counter += 1

                    if win_counter == 4:
                        print("you won")
                        self.board = [
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"]
                        ]
                        win_counter = 0
                        return True
                    else:
                        win_counter = 0

                    for i in range(0, 4):
                        if r + i > 5 or c - i < 0:
                            break
                        elif chip == self.board[r + i][c - i]:
                            win_counter += 1

                    if win_counter == 4:
                        print("you won")
                        self.board = [
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"]
                        ]
                        win_counter = 0
                        return True
                    else:
                        win_counter = 0

                    for i in range(0, 4):
                        if r - i < 0 or c - i < 0:
                            break
                        elif chip == self.board[r - i][c - i]:
                            win_counter += 1

                    if win_counter == 4:
                        print("you won")
                        self.board = [
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--"]
                        ]
                        win_counter = 0
                        return True
                    else:
                        win_counter = 0

    def open_rows(self):  # checks the rows a chip can be placed
        self.available_cols = []
        for r in range(0, 1):
            for c in range(0, 6):
                if self.board[r][c] == "--":  # checks if col is full
                    self.available_cols.append(c)  # appends available col to a list


