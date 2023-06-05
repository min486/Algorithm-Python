from collections import deque

n = int(input())
k = int(input())
arr = [[0] * (n+1) for _ in range(n+1)]  # 맵 정보
dr_li = []  # 방향 회전 정보

for _ in range(k):
    a, b = map(int, input().split())
    arr[a][b] = 1  # 사과 있는 곳

l = int(input())
for _ in range(l):
    x, c = input().split()
    dr_li.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(우, 하, 좌, 상)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(dr, c):
    if c == 'L':
        dr = (dr - 1) % 4
    else:
        dr = (dr + 1) % 4
    return dr

def solve():
    x, y = 1, 1  # 뱀의 머리 위치
    arr[x][y] = 2  # 뱀이 존재하는 위치는 2로 표시
    dr = 0  # 처음에는 동쪽을 보고 있음
    time = 0  # 시작한 뒤에 지난 '초' 시간
    idx = 0  # 다음에 회전할 정보
    q = deque([(x, y)])  # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx = x + dx[dr]
        ny = y + dy[dr]
        # 범위 안에 있고, 뱀의 몸통이 없는 위치면
        if 1 <= nx <= n and 1 <= ny <= n and arr[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                q.append((nx, ny))
                xx, yy = q.popleft()
                arr[xx][yy] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if arr[nx][ny] == 1:
                arr[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪히면
        else:
            time += 1
            break
        x, y = nx, ny  # 다음 위치로 머리 이동
        time += 1
        if idx < l and time == dr_li[idx][0]:  # 회전할 시간인 경우 회전
            dr = turn(dr, dr_li[idx][1])
            idx += 1
    return time

print(solve())