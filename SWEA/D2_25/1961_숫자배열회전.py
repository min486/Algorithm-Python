def rotate(a, b):
    for i in range(n):
        for j in range(n):
            b[i][j] = a[n-j-1][i]

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    rotate_90 = [[0]*n for _ in range(n)]
    rotate_180 = [[0]*n for _ in range(n)]
    rotate_270 = [[0]*n for _ in range(n)]

    rotate(arr, rotate_90)
    rotate(rotate_90, rotate_180)
    rotate(rotate_180, rotate_270)

    print(f'#{tc}')
    for k in range(n):
        print(*rotate_90[k], sep='', end=' ')
        print(*rotate_180[k], sep='', end=' ')
        print(*rotate_270[k], sep='')