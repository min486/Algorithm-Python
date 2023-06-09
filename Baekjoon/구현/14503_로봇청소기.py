# 상 / 우 / 하 / 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solve(x, y, d):
    global result
    if data[x][y] == 0:
        data[x][y] = 2
        result += 1
    # 주변 4칸 빈 칸 있는지 확인
    for i in range(4):
        dr = (d + 3) % 4  # 반시계 방향으로 90도 회전
        nx = x + dx[dr]
        ny = y + dy[dr]
        if data[nx][ny] == 0:
            solve(nx, ny, dr)
            return
        d = dr
    # 주변 4칸 빈 칸 없는 경우
    dr = (d + 2) % 4  # 뒤쪽 위치
    nx = x + dx[dr]
    ny = y + dy[dr]
    if data[nx][ny] == 1:  # 후진할 수 없으면 리턴
        return
    solve(nx, ny, d)

n, m = map(int, input().split())
r, c, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
result = 0

solve(r, c, d)

print(result)