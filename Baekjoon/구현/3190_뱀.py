n = int(input())
k = int(input())
alst = [tuple(map(int, input().split())) for _ in range(k)]
l = int(input())
dlst = [input().split() for _ in range(l)]

di, dj = [-1,0,1,0], [0,1,0,-1] # 시계방향으로 방향정의
dtbl = [0]*(10001)              # 방향전환에 사용되는 룩업테이블 생성
for sec, turn in dlst:
    dtbl[int(sec)] = turn

dr = 1                          # 오른쪽 방향
snake = [(1,1)]                 # 좌측상단
ans = 0                         # 0초

while True:
    ans += 1 # 1초 경과
    ci, cj = snake[-1]  # 현재 머리좌표
    ni, nj = ci + di[dr], cj + dj[dr]  # 진행방으로 한 칸 이동
    # 벽에 부딪혔거나, 뱀 몸에 부딪힌 경우 종료
    if 1 <= ni <= n and 1 <= nj <= n and (ni, nj) not in snake:
        snake.append((ni,nj))  # 머리위치[-1]에 이동좌표 확장
        if (ni,nj) in alst:
            alst.remove((ni,nj))
        else:
            snake.pop(0)  # 꼬리부분 제거
        # 방향전환
        if dtbl[ans] == 'D':  # 우회전
            dr = (dr+1) % 4
        elif dtbl[ans] == 'L':  # 좌회전
            dr = (dr+3) % 4
    else:  # 종료
        break
print(ans)