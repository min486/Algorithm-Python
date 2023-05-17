def check():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                # 우측, 하단, 하단 우측 대각선, 하단 좌측 대각선
                for di, dj in ((0, 1), (1, 0), (1, 1), (1, -1)):
                    for mul in range(5):
                        ni, nj = i + di*mul, j + dj*mul
                        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'o':
                            continue
                        else:
                            break
                    else:
                        return 'YES'
    return 'NO'

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [input() for _ in range(n)]

    result = check()
    print(f'#{tc} {result}')