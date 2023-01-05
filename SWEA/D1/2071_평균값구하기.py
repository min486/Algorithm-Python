T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    add = 0
    
    for i in nums:
        add += i
    result = round(add / 10)
        
    print(f'#{tc} {result}')