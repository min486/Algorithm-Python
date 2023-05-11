from collections import deque

def bfs(s, e):
    deq = deque()
    deq.append(s)
    visit[s] = 1

    while deq:
        x = deq.popleft()

        for adj in graph[x]:
            if visit[adj] == 0:
                deq.append(adj)
                visit[adj] += visit[x] + 1  # 촌수를 세기 위해 1씩 증가

        if x == e:
            return visit[e] - 1  # 촌수는 자신 포함하지 않으므로 -1
        
    return -1  # 도달하지 못할 때 (촌수 계산 불가)

n = int(input())
s, e = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

visit = [0] * (n+1)

print(bfs(s, e))