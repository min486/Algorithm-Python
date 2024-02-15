from collections import deque

def bfs(si, sj, ei, ej):
    q = deque()
    v = [[0] * M for _ in range(N)]

    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        if (ci,cj) == (ei,ej):
            return v[ei][ej]

        # 4방향, 범위내, 미방문, arr==1
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

res = bfs(0, 0, N-1, M-1)
print(res)