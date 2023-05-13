di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    i, j, cnt, dr = 0, 0, 1, 0
    arr[i][j] = cnt
    cnt += 1

    while cnt <= n*n:
        ni, nj = i + di[dr], j + dj[dr]
        # 범위 이내이고, 방문한 곳 아니면
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0:
            i, j = ni, nj
            arr[i][j] = cnt
            cnt += 1
        else:
            dr = (dr+1) % 4

    print(f'#{tc}')
    for li in arr:
        print(*li)