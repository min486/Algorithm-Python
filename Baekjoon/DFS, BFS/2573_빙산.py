from collections import deque

def bfs(si, sj, v):
    q = deque()

    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci,cj = q.popleft()
        # 4방향, 미방문, > 0, 범위내는 생략가능
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if v[ni][nj] == 0 and arr[ni][nj] > 0:
                q.append((ni,nj))
                v[ni][nj] = 1 

def solve():
    for year in range(1, 100000):
        # 4방향 0의 개수 카운트
        cnt_zero = [[0] * M for _ in range(N)]
        for i in range(1, N-1):
            for j in range(1, M-1):
                if arr[i][j] == 0:  # 바다면
                    continue
                for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):  # 빙산이면
                    ni, nj = i+di, j+dj
                    if arr[ni][nj] == 0:
                        cnt_zero[i][j] += 1

        # 높이 낮추기
        for i in range(1, N-1):
            for j in range(1, M-1):
                if cnt_zero[i][j] > 0:
                    arr[i][j] = max(0, arr[i][j] - cnt_zero[i][j])

        # 빙산 덩어리 개수 카운트
        v = [[0] * M for _ in range(N)]
        cnt = 0
        for i in range(1, N-1):
            for j in range(1, M-1):
                if v[i][j] == 0 and arr[i][j] > 0:
                    bfs(i, j, v)
                    cnt += 1
                    if cnt > 1:  # 두 덩어리 이상이면
                        return year
        if cnt == 0:  # 덩어리 개수 0개이면
            return 0
    return -1  # 예외처리 (생략가능)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

res = solve()
print(res)