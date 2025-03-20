from collections import deque

def bfs(si,sj):
	q = deque()

	q.append((si, sj))
	v[si][sj] = 1
	cnt = 1
    
	while q:
		ci, cj = q.popleft()

		for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
			ni, nj = ci+di, cj+dj
			if 0<=ni<n and 0 <=nj<n and v[ni][nj]==0 and arr[ni][nj]==1:
				q.append((ni,nj))
				v[ni][nj] = 1
				cnt += 1
	
	return cnt

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

v = [[0]*n for _ in range(n)]
ans = []

for i in range(n):
    for j in range(n):
        if arr[i][j]==1 and v[i][j]==0:
            ans.append(bfs(i,j))
            
ans.sort()
print(len(ans), *ans, sep='\n')