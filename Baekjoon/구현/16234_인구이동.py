from collections import deque

# 상 / 우 / 하 / 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def solve(x, y, idx):
    u_li = []  # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    u_li.append((x, y))
    q = deque()  # 너비 우선 탐색(BFS)을 위한
    q.append((x, y))
    union[x][y] = idx  # 현재 연합의 번호 할당
    total = arr[x][y]  # 현재 연합의 전체 인구 수
    cnt = 1  # 현재 연합의 국가 수

    # 큐가 빌 때까지 반복(BFS)
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1 :
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(arr[nx][ny] - arr[x][y]) <= r :
                    q.append((nx, ny))
                    # 연합에 추가
                    union[nx][ny] = idx
                    total += arr[nx][ny]
                    cnt += 1
                    u_li.append((nx, ny))

    # 연합 국가끼리 인구를 분배
    for i, j in u_li :
        arr[i][j] = total // cnt
    return cnt

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
day = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    idx = 0

    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                solve(i, j, idx)
                idx += 1

    # 모든 인구 이동이 끝난 경우
    if idx == n * n :
        break
    day += 1

print(day)