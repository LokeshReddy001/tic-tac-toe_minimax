from board import Board

def minimax(node, depth, maxmizingPlayer):
    """
        source - https://en.wikipedia.org/wiki/Minimax#Pseudocode
    """

    if depth == 0 or node.is_terminal():
        return node.evaluate(), None

    if maxmizingPlayer:
        best_value = float('-inf')
        best_move = None
        for move in node.get_moves():
            new_node = node.make_move(move)
            value, _ = minimax(new_node, depth - 1, False)
            if value > best_value:
                best_value = value
                best_move = move
        return best_value, best_move
    else:
        best_value = float('inf')
        best_move = None
        for move in node.get_moves():
            new_node = node.make_move(move)
            value, _ = minimax(new_node, depth - 1, True)
            if value < best_value:
                best_value = value
                best_move = move
        return best_value, best_move


def get_human_move(node):
    while True:
        try:
            move = int(input('Enter your move(1-9): '))
            if move in node.get_moves():
                return move
            print('Invalid move')
        except ValueError:
            print('Invalid move')


def game():
    turn = int(input("Type 0 if you want to play first, 1 otherwise: "))
    root = Board('---------', turn)
    while not root.is_terminal():
        print(root)
        if root.turn == 0:
            move = get_human_move(root)
        else:
            value, move = minimax(root, 9, root.turn == 0)
        root = root.make_move(move)
    print(root)
    if root.evaluate() == 1:
        print('You win')
    elif root.evaluate() == -1:
        print('You lose')
    else:
        print('Draw')

game()