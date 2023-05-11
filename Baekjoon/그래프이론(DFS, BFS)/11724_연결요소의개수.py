def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        now = stack.pop()
        for adj in graph[now]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
result = 0

for j in range(1, n+1):
    if not visited[j]:
        dfs(j)
        result += 1

print(result)