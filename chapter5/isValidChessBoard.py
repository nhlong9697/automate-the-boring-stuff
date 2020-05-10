chess_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def is_valid_chess_board(chess_board):
    is_one_king = True
    is_valid_space = True
    is_black_or_white = True
    number_white_king = 0
    number_black_king = 0
    for v in chess_board.values():
        if (v[0] != 'b') and (v[0] != 'w'):
            is_black_or_white = False
        if (v == 'bking'):
            number_black_king += 1
        if (v == 'wking'):
            number_white_king += 1
    if number_black_king > 1 or number_white_king > 1:
        is_one_king = False

    for k in chess_board.keys():
        if int(k[0]) > 8 or ord('h') < ord(k[1]):
            is_valid_space = False

    is_valid_chess_board = is_black_or_white and is_one_king and is_valid_space
    return is_valid_chess_board
print(str(is_valid_chess_board(chess_board)))
