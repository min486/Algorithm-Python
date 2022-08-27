T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]
    
    mx = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            dead = 0
            for k in range(M):
                for l in range(M):
                    dead += area[i+k][j+l]
            if dead > mx:
                mx = dead
                
    print(f'#{tc} {mx}')