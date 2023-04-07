from collections import deque

def bfs(s, e):
    deq = deque()
    deq.append(s)  # 초기데이터 삽입
    visit[s] = 1  # 방문 표시

    while deq:
        x = deq.popleft()

        if x == e:
            return visit[e] - 1

        # 3방향, 범위내 and 미방문
        for i in (x-1, x+1, x*2):
            if 0 <= i <= 200000 and visit[i] == 0:
                deq.append(i)
                visit[i] = visit[x] + 1

n, k = map(int, input().split())
visit = [0] * 200001

print(bfs(n, k))