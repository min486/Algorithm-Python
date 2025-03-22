from collections import deque

def bfs(si,sj,ei,ej):
    q = deque()

    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci,cj = q.popleft()

        if (ci,cj) == (ei,ej):
            return v[ei][ej]
        
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj

            if 0<=ni<n and 0<=nj<m and v[ni][nj]==0 and arr[ni][nj]==1:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

v = [[0]*m for _ in range(n)]

ans = bfs(0,0,n-1,m-1)
print(ans)