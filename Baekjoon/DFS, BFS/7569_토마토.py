from collections import deque

def bfs():
    q = deque()
    v = [[[0] * M for _ in range(N)] for _ in range(H)]

    cnt = 0  # 안익은 토마토 카운트
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1:  # 익은 토마토
                    q.append((h,i,j))
                    v[h][i][j] = 1
                elif arr[h][i][j] == 0:  # 안익은 토마토
                    cnt += 1

    while q:
        ch, ci, cj = q.popleft()

        # 6방향, 범위내, 미방문, arr==0
        for dh,di,dj in ((0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(-1,0,0),(1,0,0)):
            nh, ni, nj = ch+dh, ci+di, cj+dj
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and v[nh][ni][nj] == 0 and arr[nh][ni][nj] == 0:
                q.append((nh,ni,nj))
                v[nh][ni][nj] = v[ch][ci][cj] + 1
                cnt -= 1

    if cnt == 0:  # 모든 토마토 익었으면
        return v[ch][ci][cj] -1
    else:  # 모든 토마토가 익지 못하면
        return -1

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

res = bfs()
print(res)