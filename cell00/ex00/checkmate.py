def find_king(board):
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell == 'K':
                return (r, c)
    return None

def checkmate(board_str):
    board_rows = board_str.strip().split('\n')
    i = 0
    while (i < len(board_rows)):
        board_rows[i] = str(board_rows[i]).strip()
        i += 1
    board = [list(row) for row in board_rows]

    king_pos = find_king(board)

    if not king_pos:
        print("Fail")
        return

    kr, kc = king_pos
    size = len(board)

    # Check Rook and Queen (RQ) vertically (up)
    r = kr - 1
    while r >= 0:
        if board[r][kc] in 'RQ':
            print("Success")
            return
        if board[r][kc] != '.': # Stop if there is a piece blocking
            break
        r -= 1

    # Check Rook and Queen (RQ) vertically (down)
    r = kr + 1
    while r < size:
        if board[r][kc] in 'RQ':
            print("Success")
            return
        if board[r][kc] != '.': # Stop if there is a piece blocking
            break
        r += 1

    # Check Rook and Queen (RQ) horizontally (left)
    c = kc - 1
    while c >= 0:
        if board[kr][c] in 'RQ':
            print("Success")
            return
        if board[kr][c] != '.': # Stop if there is a piece blocking
            break
        c -= 1

    # Check Rook and Queen (RQ) horizontally (right)
    c = kc + 1
    while c < size:
        if board[kr][c] in 'RQ':
            print("Success")
            return
        if board[kr][c] != '.': # Stop if there is a piece blocking
            break
        c += 1

    # Check Bishop and Queen (BQ) diagonally (top-left)
    r, c = kr - 1, kc - 1
    while r >= 0 and c >= 0:
        if board[r][c] in 'BQ':
            print("Success")
            return
        if board[r][c] != '.': # Stop if there is a piece blocking
            break
        r -= 1
        c -= 1

    # Check Bishop and Queen (BQ) diagonally (top-right)
    r, c = kr - 1, kc + 1
    while r >= 0 and c < size:
        if board[r][c] in 'BQ':
            print("Success")
            return
        if board[r][c] != '.': # Stop if there is a piece blocking
            break
        r -= 1
        c += 1

    # Check Bishop and Queen (BQ) diagonally (bottom-left)
    r, c = kr + 1, kc - 1
    while r < size and c >= 0:
        if board[r][c] in 'BQ':
            print("Success")
            return
        if board[r][c] != '.': # Stop if there is a piece blocking
            break
        r += 1
        c -= 1

    # Check Bishop and Queen (BQ) diagonally (bottom-right)
    r, c = kr + 1, kc + 1
    while r < size and c < size:
        if board[r][c] in 'BQ':
            print("Success")
            return
        if board[r][c] != '.': # Stop if there is a piece blocking
            break
        r += 1
        c += 1

    # Check Pawn (P) diagonally (top-left)
    if kr > 0 and kc > 0 and board[kr + 1][kc - 1] == 'P':
        print("Success")
        return

    # Check Pawn (P) diagonally (top-right)
    if kr > 0 and kc < size - 1 and board[kr + 1][kc + 1] == 'P':
        print("Success")
        return

    print("Fail")