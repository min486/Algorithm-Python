T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    result = A + B
    
    if result == 24:
        result = 0
    if result > 24:
        result -= 24
    
    print(f'#{tc} {result}')