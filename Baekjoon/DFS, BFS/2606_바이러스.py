n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False] * (n+1)
visit[1] = True
stack = [1]

while len(stack) != 0:
    now = stack.pop()

    for adj in graph[now]:
        if not visit[adj]:
            visit[adj] = True
            stack.append(adj)

result = sum(visit) - 1
print(result)