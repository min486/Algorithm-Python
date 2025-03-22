def dfs(c):
    global ans

    ans += 1
    v[c] = 1

    for n in adj[c]:
        if v[n] == 0:
            dfs(n)

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

v = [0]*(n+1)
ans = 0
dfs(1)

print(ans-1)