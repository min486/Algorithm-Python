from collections import deque

def dfs(a):
    result_dfs.append(a)  # 방문 결과 추가
    visit[a] = 1  # 방문 표시

    for adj in graph[a]:
        if visit[adj] == 0:  # 방문하지 않았으면
            dfs(adj)

def bfs(a):
    deq = deque()
    deq.append(a)

    result_bfs.append(a)
    visit[a] = 1

    while deq:  # deq 빌때까지 진행
        now = deq.popleft()

        for adj in graph[now]:
            if visit[adj] == 0:
                deq.append(adj)
                result_bfs.append(adj)
                visit[adj] = 1

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# 오름차순 정렬 (정점 번호 작은 것 먼저 방문)
for i in range(1, n+1):
    graph[i].sort()

visit = [0] * (n+1)
result_dfs = []
dfs(v)

visit = [0] * (n+1)
result_bfs = []
bfs(v)

print(*result_dfs)
print(*result_bfs)