from collections import deque

# 4방향 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
	deq = deque()
	deq.append((a, b))

	visit[a][b] = 1  # 방문 표시
	cnt = 1  # 처음 bfs함수 내로 들어온 곳도 세기 위해 1로 초기화

	while deq:
		x, y = deq.popleft()
		
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			# 지도 범위를 넘지 않으면
			if 0 <= nx < n and 0 <= ny < n:
				# 집이 있고 and 방문하지 않은 곳이면
				if graph[nx][ny] == '1' and visit[nx][ny] == 0:
					visit[nx][ny] = 1  # 방문 표시
					cnt += 1  # 집의 수 증가
					deq.append((nx, ny))
	
	return cnt  # 단지내 집의 수 리턴

n = int(input())

graph = [list(input()) for _ in range(n)]
visit = [[0] * n for _ in range(n)]
result_cnt = []  # 각 단지내 집의 수를 넣기 위한 리스트

for i in range(n):
	for j in range(n):
		# 집이 있고 and 방문하지 않은 곳이면
		if graph[i][j] == '1' and visit[i][j] == 0:
			result_cnt.append(bfs(i, j))

print(len(result_cnt))  # 단지 개수

result_cnt.sort()  # 오름차순 정렬

for re in result_cnt:
	print(re)