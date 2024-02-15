from collections import deque

def bfs(s, e):
    q = deque()
    v = [0] * (F+1)

    q.append(s)
    v[s] = 1  # 1부터 시작

    while q:
        c = q.popleft()
        if c == e:
            return v[e] - 1  # 1부터 시작했으니 -1 빼기
            
        # 2방향, 범위내, 미방문
        for n in (c+U, c-D):
            if 1 <= n <= F and v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1

    return 'use the stairs'  # 목적지 갈 수 없으면

F, S, G, U, D = map(int, input().split())

res = bfs(S, G)
print(res)