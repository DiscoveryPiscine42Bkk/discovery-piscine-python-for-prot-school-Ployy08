def find_king(board):
    r = 0
    while r < len(board):
        c = 0
        while c < len(board[r]):
            if board[r][c] == 'K':
                return (r, c)
            c += 1
        r += 1
    return None

def checkmate(board_str):
    # การตัดเป็นแถว
    board = board_str.strip().split()

    king_pos = find_king(board)

    if not king_pos:
        print("Fail")
        return

    #kr,kc รับค่า R C
    kr, kc = king_pos
    #ความยาว,ขนาดของบอร์ด ยาวเท่าไหร่ 
    size = len(board)

    # kr-1หาทิศบน
    r = kr - 1
    while r >= 0:
        if board[r][kc] in 'RQ':
            print("Success")
            return
        if board[r][kc] != '.': 
            break
        r -= 1

    # kr+1 หาข้างล่าง
    r = kr + 1
    while r < size:
        if board[r][kc] in 'RQ':
            print("Success")
            return
        if board[r][kc] != '.': 
            break
        r += 1

    # kc-1 หาทางซ้าย
    c = kc - 1
    while c >= 0:
        if board[kr][c] in 'RQ':
            print("Success")
            return
        if board[kr][c] != '.':
            break
        c -= 1

    # kc+1 หาทางขวา
    c = kc + 1
    while c < size:
        if board[kr][c] in 'RQ':
            print("Success")
            return
        if board[kr][c] != '.': 
            break
        c += 1

    # kr-1,kc-1 หาทิศทางซ้ายบน
    r, c = kr - 1, kc - 1
    while r >= 0 and c >= 0:
        if board[r][c] in 'BQ':
            print("Success")
            return
        if board[r][c] != '.': 
            break
        r -= 1
        c -= 1

    # kr-1,kc+1 หาทิศทางขวาบน
    r, c = kr - 1, kc + 1
    while r >= 0 and c < size:
        if board[r][c] in 'BQ':
            print("Success")
            return
        if board[r][c] != '.':
            break
        r -= 1
        c += 1

    # kr+1,kc-1 หาทิศทางซ้ายล่าง
    r, c = kr + 1, kc - 1
    while r < size and c >= 0:
        if board[r][c] in 'BQ':
            print("Success")
            return
        if board[r][c] != '.': 
            break
        r += 1
        c -= 1

    # kr+1,kc+1 หาทิศทางขวาล่าง
    r, c = kr + 1, kc + 1
    while r < size and c < size:
        if board[r][c] in 'BQ':
            print("Success")
            return
        if board[r][c] != '.': 
            break
        r += 1
        c += 1

    # หาทิศทางซ้ายบนตัวp
    if kr > 0 and kc > 0 and board[kr + 1][kc - 1] == 'P':
        print("Success")
        return

    # หาทิศทางขวาบนตัวp
    if kr > 0 and kc < size - 1 and board[kr + 1][kc + 1] == 'P':
        print("Success")
        return

    print("Fail")