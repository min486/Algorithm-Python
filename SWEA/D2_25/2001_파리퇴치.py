t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            cnt = 0
            for k in range(i, i+m):
                for l in range(j, j+m):
                    cnt += arr[k][l]
            if cnt > ans:
                ans = cnt

    print(f'#{tc} {ans}')