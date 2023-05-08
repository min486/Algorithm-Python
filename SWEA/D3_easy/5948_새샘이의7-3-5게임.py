T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    totals = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] not in totals:
                    totals.append(nums[i] + nums[j] + nums[k])
    
    result = sorted(totals)[-5]
    print(f'#{tc} {result}')