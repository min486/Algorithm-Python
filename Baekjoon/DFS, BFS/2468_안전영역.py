from collections import deque

def bfs(i, j, h):
    deq = deque()
    deq.append((i, j))
    visit[i][j] = 1

    while deq:
        x, y = deq.popleft()
        # 4방향
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x+dx, y+dy
            # 범위내, 미방문, 높이 > h(물 높이)
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and graph[nx][ny] > h:
                deq.append((nx, ny))
                visit[nx][ny] = 1

def solve(h):  # 물 높이에 대해 잠기지 않는 영역 개수 리턴
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0 and graph[i][j] > h:
                bfs(i, j, h)
                cnt += 1
    return cnt

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = 0
for rain_h in range(100):
    visit = [[0] * n for _ in range(n)]
    result = max(result, solve(rain_h))  # 최대 개수

print(result)