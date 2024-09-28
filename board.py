RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
CYAN = '\033[96m'
WHITE = '\033[97m'
PURPLE = '\033[95m'
RESET = '\033[0m'

class Board:
    def __init__(self, s, turn=0):
        self.state = s
        self.turn = turn
        self.turn_to_sym = {0: 'X', 1: 'O'}

    def get_moves(self):
        return [i for i in range(len(self.state)) if self.state[i] == '-']

    def make_move(self, pos):        
        new_state = self.state[:pos] + self.turn_to_sym[self.turn] + self.state[pos + 1:]
        return Board(new_state, 1-self.turn)
    
    def is_terminal(self):
        return self.evaluate() != 0 or '-' not in self.state
        
    def evaluate(self):
        matrix = [[self.state[i] for i in range(j, j+3)] for j in range(0, 9, 3)]
        
        for row in matrix:
            if row[0] == row[1] == row[2] == 'X':
                return 1
            if row[0] == row[1] == row[2] == 'O':
                return -1
        
        for col in range(3):
            if matrix[0][col] == matrix[1][col] == matrix[2][col] == 'X':
                return 1
            if matrix[0][col] == matrix[1][col] == matrix[2][col] == 'O':
                return -1
        
        if matrix[0][0] == matrix[1][1] == matrix[2][2] == 'X':
            return 1
        if matrix[0][0] == matrix[1][1] == matrix[2][2] == 'O':
            return -1

        if matrix[0][2] == matrix[1][1] == matrix[2][0] == 'X':
            return 1
        if matrix[0][2] == matrix[1][1] == matrix[2][0] == 'O':
            return -1

        return 0

            
    def __str__(self):
        board = ""
        for i in range(9):
            if self.state[i] == '-':
                board += WHITE + str(i) + RESET
            elif self.state[i] == 'X':
                board += CYAN + 'X' + RESET
            else:
                board += PURPLE + 'O' + RESET
            if i % 3 == 2:
                board += "\n"
            else:
                board += " | "
        
        separator = "---------\n"
        return f"\n{board.split(chr(10)[0])[0]}\n{separator}{board.split(chr(10)[0])[1]}\n{separator}{board.split(chr(10)[0])[2]}\n"
