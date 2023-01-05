T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    result = 0
    
    for i in nums:
        if i % 2 == 1:
            result += i
            
    print(f'#{tc} {result}')