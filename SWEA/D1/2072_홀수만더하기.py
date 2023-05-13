t = int(input())

for tc in range(1, t+1):
    li = list(map(int, input().split()))
    result = 0
    
    for i in li:
        if i % 2 == 1:
            result += i
            
    print(f'#{tc} {result}')