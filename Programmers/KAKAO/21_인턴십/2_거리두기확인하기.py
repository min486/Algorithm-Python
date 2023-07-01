from collections import deque

def bfs(place, x, y):
    visited = [[False] * 5 for _ in range(5)]
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True

    while q:
        x, y, dist = q.popleft()
        if dist == 2:
            continue
        for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):  # 상/하/좌/우 탐색
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nx][ny]:
                    continue
                if place[nx][ny] =='X':
                    continue
                if place[nx][ny] == 'P':
                    return False
                if place[nx][ny] == 'O':
                    q.append((nx, ny, dist + 1))
                    visited[nx][ny] = True
    return True

def check(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                if bfs(place, r, c) == False:  # 거리두기 미준수
                    return False
    return True  # 거리두기 준수       

def solution(places):
    answer = []

    for place in places:
        if check(place):  # 각 대기실 확인
            answer.append(1)
        else:
            answer.append(0)
    return answer