from collections import deque
import copy

def three_wall(cnt):  # 벽 세우기
    if cnt == 3:  # 벽 3개 세웠으면 bfs
        bfs()
        return  # 벽 3개 중 1개 위치 다음으로 움직이도록 종료 (벽 함수 4번 호출된 상태)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                # bfs 끝난 후 세웠던 벽 원래대로 (1 -> 0)
                three_wall(cnt+1) 
                graph[i][j] = 0

def bfs():
    deq = deque([])
    new_graph = copy.deepcopy(graph)  # 깊은 복사 (원래의 배열에 영향 안미침)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:  # 바이러스면 deq에 더하기
                deq.append([i,j])
    while deq:
        x,y = deq.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and new_graph[nx][ny] == 0:
                new_graph[nx][ny] = 2
                deq.append([nx,ny])    
    global answer
    cnt = 0

    for i in range(n):  
        cnt += new_graph[i].count(0)  # 각 행별 안전영역 누적
    answer = max(answer,cnt)  # 최댓값 갱신

n, m = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0
three_wall(0)

print(answer)