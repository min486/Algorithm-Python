def dfs(c):
    global res

    res += 1
    v[c] = 1

    for n in adj[c]:
        if v[n] == 0:
            dfs(n)

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

res = 0
v = [0] * (N+1)
dfs(1)
print(res-1)