from collections import deque

def dfs(c):
    res_dfs.append(c)  # 방문 노드 추가
    v[c] = 1  # 방문 표시

    for n in adj[c]:
        if v[n] == 0:  # 방문하지 않았으면
            dfs(n)

def bfs(s):
    q = deque()

    q.append(s)
    res_bfs.append(s)
    v[s] = 1

    while q:  # q 빌때까지 진행
        c = q.popleft()

        for n in adj[c]:
            if v[n] == 0:
                q.append(n)
                res_bfs.append(n)
                v[n] = 1

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for i in range(1, N+1):  # 오름차순 정렬
    adj[i].sort()

v = [0] * (N+1)
res_dfs = []
dfs(V)

v = [0] * (N+1)
res_bfs = []
bfs(V)

print(*res_dfs)
print(*res_bfs)