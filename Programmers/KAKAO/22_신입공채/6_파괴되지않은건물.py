ATTACK = 1
RECOVER = 2

def solution(board, skill):
    update(board, skill)
    answer = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if is_not_destroyed(board, r, c):
                answer += 1
    return answer

def update(board, skill):
    diff = [[0]*(len(board[0]) + 1) for _ in range(len(board) + 1)]  # r2+1 / c2+1는 범위를 초과하므로
    for type, r1, c1, r2, c2, degree in skill:
        d = -degree if type == ATTACK else degree
        diff[r1][c1] += d
        diff[r1][c2+1] += -d
        diff[r2+1][c1] += -d
        diff[r2+1][c2+1] += d

    # board (4 x 5) 라고 하면
    for r in range(len(board)):  # 0~3
        for c in range(1, len(board[0])):  # 1~4
            diff[r][c] += diff[r][c-1]
    for r in range(len(board[0])):  # 0~4
        for c in range(1, len(board)):  # 1~3
            diff[c][r] += diff[c-1][r]
            
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] += diff[r][c]

def is_not_destroyed(board, r, c):
    return board[r][c] > 0