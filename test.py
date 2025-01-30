# 駒の移動ルール判定
def is_valid_move(board, start, end):
    sx, sy = start
    ex, ey = end
    piece = board[sx][sy]
    target = board[ex][ey]

    # 盤外チェック
    if not (0 <= sx < 9 and 0 <= sy < 9 and 0 <= ex < 9 and 0 <= ey < 9):
        return False

    # 移動先に自分の駒がないか
    if (piece.isupper() and target.isupper()) or (piece.islower() and target.islower()):
        return False

    # 駒ごとの移動ルール
    if piece.lower() == "p":  # 歩
        return is_valid_pawn_move(start, end, piece.isupper())
    elif piece.lower() == "l":  # 香車
        return is_valid_lance_move(board, start, end, piece.isupper())
    elif piece.lower() == "n":  # 桂馬
        return is_valid_knight_move(start, end, piece.isupper())
    elif piece.lower() == "s":  # 銀
        return is_valid_silver_move(start, end, piece.isupper())
    elif piece.lower() == "g" or piece.lower() == "p+":  # 金または成歩
        return is_valid_gold_move(start, end, piece.isupper())
    elif piece.lower() == "k":  # 玉
        return is_valid_king_move(start, end)
    elif piece.lower() == "r":  # 飛車
        return is_valid_rook_move(board, start, end)
    elif piece.lower() == "b":  # 角
        return is_valid_bishop_move(board, start, end)
    elif piece.lower() in ["r+", "b+"]:  # 龍王または龍馬
        return is_valid_promoted_piece_move(board, start, end, piece.lower())
    return False

# 駒ごとの具体的な移動ルール
def is_valid_pawn_move(start, end, is_upper):
    sx, sy = start
    ex, ey = end
    direction = -1 if is_upper else 1
    return ex == sx + direction and ey == sy

def is_valid_lance_move(board, start, end, is_upper):
    sx, sy = start
    ex, ey = end
    direction = -1 if is_upper else 1
    if sy != ey:
        return False
    # 中間に駒がないか確認
    step = direction
    for x in range(sx + step, ex, step):
        if board[x][sy] != "":
            return False
    return True

def is_valid_knight_move(start, end, is_upper):
    sx, sy = start
    ex, ey = end
    direction = -1 if is_upper else 1
    return ex == sx + 2 * direction and abs(ey - sy) == 1

def is_valid_silver_move(start, end, is_upper):
    sx, sy = start
    ex, ey = end
    direction = -1 if is_upper else 1
    return (abs(ex - sx) == 1 and abs(ey - sy) == 1) or (ex == sx + direction and ey == sy)

def is_valid_gold_move(start, end, is_upper):
    sx, sy = start
    ex, ey = end
    direction = -1 if is_upper else 1
    return (
        (abs(ex - sx) == 1 and ey == sy) or  # 前後左右
        (ex == sx + direction and abs(ey - sy) <= 1)  # 前
    )

def is_valid_king_move(start, end):
    sx, sy = start
    ex, ey = end
    return abs(ex - sx) <= 1 and abs(ey - sy) <= 1

def is_valid_rook_move(board, start, end):
    sx, sy = start
    ex, ey = end
    if sx != ex and sy != ey:
        return False
    # 中間に駒がないか確認
    if sx == ex:  # 横移動
        step = 1 if ey > sy else -1
        for y in range(sy + step, ey, step):
            if board[sx][y] != "":
                return False
    else:  # 縦移動
        step = 1 if ex > sx else -1
        for x in range(sx + step, ex, step):
            if board[x][sy] != "":
                return False
    return True

def is_valid_bishop_move(board, start, end):
    sx, sy = start
    ex, ey = end
    if abs(ex - sx) != abs(ey - sy):
        return False
    # 中間に駒がないか確認
    step_x = 1 if ex > sx else -1
    step_y = 1 if ey > sy else -1
    for i in range(1, abs(ex - sx)):
        if board[sx + i * step_x][sy + i * step_y] != "":
            return False
    return True

def is_valid_promoted_piece_move(board, start, end, piece):
    # 成り駒は金と同じ動き
    return is_valid_gold_move(start, end, piece.isupper())
