from collections import deque

def bfs(si, sj, h):
    q = deque()

    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        # 4방향, 범위내, 미방문, 높이 > h
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] > h:
                q.append((ni, nj))
                v[ni][nj] = 1

def solve(h):  # h높이에 대해 잠기지 않는 영역 개수 리턴
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0 and arr[i][j] > h:
                bfs(i, j, h)
                cnt += 1
    return cnt

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

res = 0
for h in range(100):
    v = [[0] * N for _ in range(N)]
    res = max(res, solve(h))
print(res)