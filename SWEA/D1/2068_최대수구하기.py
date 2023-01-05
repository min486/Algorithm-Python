T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    result = max(nums)
    
    print(f'#{tc} {result}')