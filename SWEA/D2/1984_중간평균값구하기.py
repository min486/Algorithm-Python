T = int(input())

for tc in range(1, T + 1):
    nums = list(map(int, input().split()))
    nums.sort()
    del nums[0]
    del nums[-1]
    
    total = sum(nums)
    avg = round(total / 8)
    
    print(f'#{tc} {avg}')