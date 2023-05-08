def check():
    for i in range(n):
        for j in range(n):
            if data[i][j] == 'o':
                # 오른쪽, 아래, 오른쪽 아래 대각선, 왼쪽 아래 대각선
                for dx, dy in ((0, 1), (1, 0), (1, 1), (1, -1)):
                    nx = i
                    ny = j
                    cnt = 0

                    while 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 'o':
                        cnt += 1
                        nx += dx
                        ny += dy

                    if cnt >= 5:
                        return 'YES'
    return 'NO'

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    data = [input() for _ in range(n)]

    print(f'#{tc} {check()}')