import Engine

'    def minimax(self, position, depth, maximizing_player):\n'
'        if depth == 0 or self.check_for_win() == True:\n'
'            return position\n'
'\n'
'        if maximizing_player:\n'
'            max_eval = -math.inf\n'
'            for child in position:\n'
'                eval = self.minimax(child, depth - 1, False)\n'
'                max_eval = max(max_eval, eval)\n'
'            return max_eval\n'
'\n'
'        else:\n'
'            min_eval = math.inf\n'
'            for child in position:\n'
'                eval = self.minimax(child, depth- 1, True)\n'
'                min_eval = min(min_eval, eval)\n'

ge = Engine.Game()


def vertical_board_evaluation():
    board_score_red = 0
    board_score_yellow = 0
    for r in range(0, 6):
        for c in range(0, 7):
            chip = ge.board[r][c]
            if chip != "--" and chip != "Yc":  # horizontal eval for red chips
                same_chip_counter = 0
                for i in range(0, 4):  # checks for 4 chips in a horizontal row
                    if r + i > 5:
                        break
                    if chip == ge.board[r + i][c]:
                        same_chip_counter += 1
                if same_chip_counter == 4:  # add 100 to score if 4 chips are in a row
                    board_score_red += 50

                same_chip_counter = 0
                for i in range(0, 3):  # checks for 3 chips in a row
                    if r + i > 5:
                        break
                    if chip == ge.board[r + i][c]:
                        same_chip_counter += 1
                if same_chip_counter == 3:  # adds 3 to score if 3 chips are in a row
                    board_score_red += 5

                for i in range(0, 2):  # checks for 2 red chips in a row
                    if r + i > 5:
                        break
                    if chip == ge.board[r + i][c]:
                        same_chip_counter += 1
                if same_chip_counter == 2:  # adds 2 to the score if 2 chips are in a row
                    board_score_red += 2

            if chip != "--" and chip != "Rc":  # horizontal eval for Yellow chips
                same_chip_counter = 0
                for i in range(0, 4):  # checks for 4 chips in a horizontal row
                    if r + i > 5:
                        break
                    if chip == ge.board[r + i][c]:
                        same_chip_counter += 1
                if same_chip_counter == 4:  # add 100 to score if 4 chips are in a row
                    board_score_yellow -= -50

                same_chip_counter = 0
                for i in range(0, 3):  # checks for 3 chips in a row
                    if r + i > 5:
                        break
                    if chip == ge.board[r + i][c]:
                        same_chip_counter += 1
                if same_chip_counter == 3:  # adds 3 to score if 3 chips are in a row
                    board_score_yellow -= -5

                for i in range(0, 2):  # checks for 2 red chips in a row
                    if r + i > 5:
                        break
                    if chip == ge.board[r + i][c]:
                        same_chip_counter += 1
                if same_chip_counter == 2:  # adds 2 to the score if 2 chips are in a row
                    board_score_yellow -= -2

    return board_score_red, board_score_yellow


def horizontal_board_evaluation():
    board_score_red = 0
    board_score_yellow = 0
    for r in range(0, 6):
        for c in range(0, 7):
            chip = ge.board[r][c]
            if chip != "--" and chip != "Yc":  # horizontal eval for red chips
                same_chip_counter = 0
                for i in range(0, 4):  # checks for 4 chips in a horizontal row
                    if c + i > 6:
                        break
                    if chip == ge.board[r][c + i]:
                        same_chip_counter += 1
                if same_chip_counter == 4:  # add 100 to score if 4 chips are in a row
                    board_score_red += 50

                same_chip_counter = 0
                for i in range(0, 3):  # checks for 3 chips in a row
                    if c + i > 6:
                        break
                    if chip == ge.board[r][c + i]:
                        same_chip_counter += 1
                if same_chip_counter == 3:  # adds 3 to score if 3 chips are in a row
                    board_score_red += 5

                for i in range(0, 2):  # checks for 2 red chips in a row
                    if c + i > 6:
                        break
                    if chip == ge.board[r][c + i]:
                        same_chip_counter += 1
                if same_chip_counter == 2:  # adds 2 to the score if 2 chips are in a row
                    board_score_red += 2

            if chip != "--" and chip != "Rc":  # horizontal eval for Yellow chips
                same_chip_counter = 0
                for i in range(0, 4):  # checks for 4 chips in a horizontal row
                    if r + i > 5:
                        break
                    if chip == ge.board[r][c + i]:
                        same_chip_counter += 1
                if same_chip_counter == 4:  # add 100 to score if 4 chips are in a row
                    board_score_yellow -= -50

                same_chip_counter = 0
                for i in range(0, 3):  # checks for 3 chips in a row
                    if c + i > 6:
                        break
                    if chip == ge.board[r][c + i]:
                        same_chip_counter += 1
                if same_chip_counter == 3:  # adds 3 to score if 3 chips are in a row
                    board_score_yellow -= -5

                for i in range(0, 2):  # checks for 2 red chips in a row
                    if c + i > 6:
                        break
                    if chip == ge.board[r][c + i]:
                        same_chip_counter += 1
                if same_chip_counter == 2:  # adds 2 to the score if 2 chips are in a row
                    board_score_yellow -= -2
            print(board_score_red)

    return board_score_red, board_score_yellow


def diagonal_board_evaluation():
    board_score_red = 0
    board_score_yellow = 0
    for r in range(0, 6):
        for c in range(0, 7):
            chip = ge.board[r][c]
            if chip == "RC":
                win_counter = 0
                for i in range(0, 4):
                    if r + i > 5 or c + i > 6:
                        break
                    elif chip == ge.board[r + i][c + i]:
                        win_counter += 1
                if win_counter == 4:
                    board_score_red = 50
                elif win_counter == 3:
                    board_score_red = 3
                elif win_counter == 2:
                    board_score_red = 2

                for i in range(0, 4):
                    if r - i < 0 or c + i > 6:
                        break
                    elif chip == ge.board[r - i][c + i]:
                        win_counter += 1
                if win_counter == 4:
                    board_score_red = 50
                elif win_counter == 3:
                    board_score_red = 3
                elif win_counter == 2:
                    board_score_red = 2

                for i in range(0, 4):
                    if r + i > 5 or c - i < 0:
                        break
                    elif chip == ge.board[r + i][c - i]:
                        win_counter += 1
                if win_counter == 4:
                    board_score_red = 50
                elif win_counter == 3:
                    board_score_red = 3
                elif win_counter == 2:
                    board_score_red = 2

                for i in range(0, 4):
                    if r - i < 0 or c - i < 0:
                        break
                    elif chip == ge.board[r - i][c - i]:
                        win_counter += 1
                if win_counter == 4:
                    board_score_red = 50
                elif win_counter == 3:
                    board_score_red = 3
                elif win_counter == 2:
                    board_score_red = 2

    return board_score_red, board_score_yellow


def final_evaluation():
    diagonal = diagonal_board_evaluation()
    horizontal = horizontal_board_evaluation()
    vertical = vertical_board_evaluation()



print(diagonal_board_evaluation())
