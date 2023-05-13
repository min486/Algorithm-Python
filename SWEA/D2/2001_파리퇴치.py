t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    mx = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            dead = 0
            for k in range(m):
                for l in range(m):
                    dead += arr[i+k][j+l]
            if dead > mx:
                mx = dead
                
    print(f'#{tc} {mx}')