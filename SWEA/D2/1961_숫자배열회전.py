T = int(input())

def rotate(a, b):
    for i in range(N):
        for j in range(N):
            b[i][j] = a[N-j-1][i]

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    rotate_90 = [[0] * N for _ in range(N)]
    rotate_180 = [[0] * N for _ in range(N)]
    rotate_270 = [[0] * N for _ in range(N)]

    rotate(data, rotate_90)
    rotate(rotate_90, rotate_180)
    rotate(rotate_180, rotate_270)

    print(f'#{tc}')
    for k in range(N) :
        print(''.join(map(str, rotate_90[k])), end=' ')
        print(''.join(map(str, rotate_180[k])), end=' ')
        print(''.join(map(str, rotate_270[k])), end=' ')
        print()