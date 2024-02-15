from collections import deque

def bfs(si, sj):
	q = deque()

	q.append((si, sj))
	v[si][sj] = 1
	cnt = 1

	while q:
		ci, cj = q.popleft()

		for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
			ni, nj = ci+di, cj+dj
			# 4방향, 범위내, 미방문, arr==1
			if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] == 1:
				q.append((ni,nj))
				v[ni][nj] = 1
				cnt += 1
	
	return cnt  # 단지내 집의 수

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

v = [[0] * N for _ in range(N)]
res = []  # 각 단지내 집의 수 리스트

for i in range(N):
	for j in range(N):
		if arr[i][j] == 1 and v[i][j] == 0:  # 집이 있고 미방문이면
			res.append(bfs(i, j))

res.sort()  # 오름차순 정렬
print(len(res), *res, sep='\n')