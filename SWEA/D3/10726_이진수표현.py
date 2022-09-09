T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    binary = bin(M) [2:]
    cnt = 0
    
    for i in binary[-N:]:
        if i == "1":
            cnt += 1
            
    if cnt == N:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')