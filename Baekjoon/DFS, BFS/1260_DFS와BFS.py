from collections import deque

def dfs(c):
    ans_dfs.append(c)
    v_dfs[c] = 1

    for n in adj[c]:
        if v_dfs[n] == 0:
            dfs(n)

def bfs(s):
    q = deque()

    q.append(s)
    ans_bfs.append(s)
    v_bfs[s] = 1
    [s] = 1

    while q:
        c = q.popleft()

        for n in adj[c]:
            if [n] == 0:
                q.append(n)
                ans_bfs.append(n)
                v_bfs[n] = 1

n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, n+1):
    adj[i].sort()

v_dfs = [0] * (n+1)
ans_dfs = []
dfs(v)

v_bfs = [0] * (n+1)
ans_bfs = []
bfs(v)

print(*ans_dfs)
print(*ans_bfs)