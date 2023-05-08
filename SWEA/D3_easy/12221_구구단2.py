T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    
    if A < 10 and B < 10:
        result = A * B
    else:
        result = -1
        
    print(f'#{tc} {result}')