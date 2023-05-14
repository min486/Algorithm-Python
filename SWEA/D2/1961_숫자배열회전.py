def rotate(a, b):
    for i in range(n):
        for j in range(n):
            b[i][j] = a[n-j-1][i]

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    rotate_90 = [[0] * n for _ in range(n)]
    rotate_180 = [[0] * n for _ in range(n)]
    rotate_270 = [[0] * n for _ in range(n)]

    rotate(data, rotate_90)
    rotate(rotate_90, rotate_180)
    rotate(rotate_180, rotate_270)

    print(f'#{tc}')
    for k in range(n):
        print(''.join(map(str, rotate_90[k])), end=' ')
        print(''.join(map(str, rotate_180[k])), end=' ')
        print(''.join(map(str, rotate_270[k])))