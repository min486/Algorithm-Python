from collections import deque

def bfs(s, e):
    deq = deque()
    deq.append(s)
    visit[s] = 1

    while deq:
        x = deq.popleft()

        if x == e:
            return visit[e] - 1

        # 2방향, 범위내 and 미방문
        for i in (x+u, x-d):
            if 1 <= i <= f and visit[i] == 0:
                deq.append(i)
                visit[i] = visit[x] + 1

    return 'use the stairs'  # 목적지로 이동 불가한 경우

f, s, g, u, d = map(int, input().split())
visit = [0] * (f+1)

print(bfs(s, g))