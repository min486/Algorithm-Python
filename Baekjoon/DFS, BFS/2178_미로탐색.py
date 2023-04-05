from collections import deque

# 4방향 탐색을 위한 변수
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))  # 출발 (0, 0)
    visit[x][y] = 1  # 다시 방문 하지 않기 위해

    while queue:
        x, y = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 넘지 않기 위해서
            if 0 <= nx < n and 0 <= ny < m:
                # 이동 가능('1') 인지 and 방문하지 않은 곳인지 판별
                if map[nx][ny] == '1' and visit[nx][ny] == 0:
                    # 전까지 방문했던 수 보다 한칸 더 간것이기에 +1
                    visit[nx][ny] = visit[x][y] + 1
                    # 도착지면 몇번만에 방문했는지 리턴
                    if nx == n-1 and ny == m-1: 
                        return visit[nx][ny]
                    queue.append((nx, ny))

n, m = map(int, input().split())
map = [list(input()) for _ in range(n)]
visit = [[0] * m for _ in range(n)]

print(bfs(0, 0))