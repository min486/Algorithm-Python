def dfs(x, y, c):
    visited[x][y] = True

    # 상/하/좌/우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 내에 있고 / 탐색하지 않았다면 탐색
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                # 탐색하는 곳이 이전에 봤던 색이면 재귀적으로 탐색
                if c == graph[nx][ny]:
                    dfs(nx, ny, c)

n = int(input())
graph = [list(input()) for _ in range(n)]  # 각 노드가 연결된 정보를 그래프로 표현
visited = [[False] * n for _ in range(n)]  # 탐색 여부
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt1 = 0  # 적록색약인이 아닌 사람이 보는 그림의 구역

# 적록색약인이 아닌 사람이 보는 그림의 구역을 dfs 통해 탐색
for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표이면 dfs로 넣어준다
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            cnt1 += 1

# G 색을 R로 변경
for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"

cnt2 = 0  # 적록색약인이 보는 그림의 구역
visited = [[False] * n for _ in range(n)]  # 탐색 여부

# 적록색약인이 보는 그림의 구역을 dfs 통해 탐색
for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표이면 dfs로 넣어준다
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            cnt2 += 1

print(cnt1, cnt2)