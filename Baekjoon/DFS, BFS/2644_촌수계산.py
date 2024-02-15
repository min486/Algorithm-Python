from collections import deque

def bfs(s, e):
    q = deque()
    v = [0] * (N+1)

    q.append(s)
    v[s] = 1

    while q:
        c = q.popleft()
        if c == e:
            return v[e] - 1  # 나와 한칸 떨어져있으면 1촌

        for n in adj[c]:  # 미방문이면
            if v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1

    return -1  # 촌수 계산할 수 없으면

N = int(input())
S, E = map(int, input().split())
M = int(input())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    p, c = map(int, input().split())
    adj[p].append(c)
    adj[c].append(p)

res = bfs(S, E)
print(res)