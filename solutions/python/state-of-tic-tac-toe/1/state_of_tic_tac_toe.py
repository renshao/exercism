def check_win(board, c):
    vector_list = [
        [(0, 0), (1, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)]
    ]
    for i in range(3):
        vector_list.append([(i, 0), (i, 1), (i, 2)])
        vector_list.append([(0, i), (1, i), (2, i)])

    wins = 0
    for vector in vector_list:
        if board[vector[0][0]][vector[0][1]] == board[vector[1][0]][vector[1][1]] == board[vector[2][0]][vector[2][1]] == c:
            wins += 1
    return wins

def gamestate(board):
    board2d = []
    xcount = 0
    ocount = 0

    for row_str in board:
        row = []
        for c in row_str:
            row.append(c)
            if c == 'X':
                xcount += 1
            elif c == 'O':
                ocount += 1
        board2d.append(row)

    if ocount > xcount:
        raise ValueError("Wrong turn order: O started")
    elif ocount < xcount - 1:
        raise ValueError("Wrong turn order: X went twice")

    xwins = check_win(board2d, 'X')
    owins = check_win(board2d, 'O')

    if xwins > 0 and owins > 0:
        raise ValueError("Impossible board: game should have ended after the game was won")
    elif xwins > 0 or owins > 0:
        return 'win'

    if xcount + ocount < 9:
        return 'ongoing'
    else:
        return 'draw'