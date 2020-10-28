import sys
import os

SQUARES = [[x + y for x in alpha for y in num] for alpha in ['ABC', 'DEF', 'GHI'] for num in ['123', '456', '789']]

ALPHA = 'ABCDEFGHI'
NUM = '123456789'

ROWS = [[x + y for y in NUM] for x in ALPHA]
COLS = [[x + y for x in ALPHA] for y in NUM]

BOARD = [x + y for x in ALPHA for y in NUM]

filename = 'sudoku.txt'

class Sudoku:
    
    def __init__(self, board):
        self.board = board
        self.possible = dict(zip([x + y for x in ALPHA for y in NUM], [[]] * 81))
        self.flag = True

    def find_row(self, pos):
        ''' Given a position on the board, returns list of the remaining positions in the same row '''
        return [pos[0] + y for y in NUM if y != pos[1]]

    def find_col(self, pos):
        ''' Given a position on the board, returns list of the remaining positions in the same column '''
        return [x + pos[1] for x in ALPHA if x != pos[0]]

    def find_square(self, pos):
        ''' Given a position on the board, returns list of the remaining positions in the same square '''
        for square in SQUARES:
            if pos in square:
                return square

    def possible_move(self, pos):
        ''' Given a position on the board, returns list of possible numbers that can fill that position.
        A number may fill the position if it is not present in any row, column or square which the position is a part of. '''
        related = set(self.find_row(pos) + self.find_col(pos) + self.find_square(pos))
        contents = [self.board[x] for x in related]
        return [x for x in range(1, 10) if x not in contents

    def is_solved(self):
        ''' Returns True if all squares are full, else False '''
        return list(self.board.values()).count(0) == 0

    def solve(self):
        ''' Solves an incomplete sudoku grid '''
        if not self.is_solved():
            if not self.solve_backtrack():
                print("\nCannot be solved\n")

    def solve_backtrack(self):
        ''' Recursively solve the Sudoku grid by using trial and error '''
        empty = self.get_empty()
        if not empty:
            return True
        possibles = self.possible_move(empty)
        for possible in possibles:
            self.board[empty] = possible
            if self.solve_backtrack():
                return True
        self.board[empty] = 0
        return False

    def get_empty(self):
        ''' Returns first empty position. If no empty positions found, return None '''
        for pos in BOARD:
            if self.board[pos] == 0:
                return pos
        return None

    def display(self):
        ''' Displays the sudoku board '''
        print()
        for i in range(0, 73, 9):
            print(*list(self.board.values())[i : i + 9])
        print()

    def is_valid(self):
        ''' Returns True if current sudoku board is a correct solution, else False '''
        return self.group_validate(ROWS) and self.group_validate(COLS) and self.group_validate(SQUARES)

    def validate(self):
        ''' Prints message for verdict of solution '''
        print("Verdict: \n")
        if self.is_valid():
            print("Answer seems totally correct, yay!")
        else:
            print("Uh, looks like something went wrong here...")
        print()

    def group_validate(self, GROUPS):
        ''' Checks if all numbers from 1 - 9 are present exactly once in the groups (rows, columns or squares) '''
        for group in GROUPS:
            contents = [self.board[pos] for pos in group]
            if not all(contents.count(i) == 1 for i in range(1, 10)):
                return False
        return True

values = []

if len(sys.argv) == 2:
    filename = sys.argv[1]

if os.path.isfile(filename):
    with open(filename) as f:
        for row in f:
            values += [int(x) for x in row.strip()]
else:
    print("No such file exists")
    sys.exit(0)

board = dict(zip(BOARD, values))

S = Sudoku(board)
print("Here is the original board:\n")
S.display()
print("\nSolving:\n")
S.solve()

S.display()
S.validate()
