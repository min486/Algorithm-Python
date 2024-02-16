N = int(input())
K = int(input())
apple_li = [tuple(map(int, input().split())) for _ in range(K)]
L = int(input())
turn_li = [input().split() for _ in range(L)]

di, dj = [-1,0,1,0], [0,1,0,-1]  # 시계방향으로 방향정의
turn_tbl = [0] * (10001)  # 방향전환에 사용
for sec, turn in turn_li:
    turn_tbl[int(sec)] = turn

dr = 1  # 오른쪽 방향
snake = [(1,1)]  # 좌측상단
res = 0  # 0초

while True:
    res += 1  # 1초 경과
    ci, cj = snake[-1]  # 현재 머리좌표
    ni, nj = ci+di[dr], cj+dj[dr]  # 진행방으로 한 칸 이동
    # 벽에 부딪히거나, 뱀 몸에 부딪힌 경우 종료
    if 1 <= ni <= N and 1 <= nj <= N and (ni, nj) not in snake:
        snake.append((ni,nj))  # 머리위치[-1]에 이동좌표 확장
        if (ni,nj) in apple_li:
            apple_li.remove((ni,nj))
        else:
            snake.pop(0)  # 꼬리부분 제거
        # 방향전환
        if turn_tbl[res] == 'D':  # 우회전
            dr = (dr+1) % 4
        elif turn_tbl[res] == 'L':  # 좌회전
            dr = (dr+3) % 4
    else:  # 종료
        break

print(res)