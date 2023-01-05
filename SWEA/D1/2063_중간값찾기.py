N = int(input())

nums = list(map(int, input().split()))
nums.sort()
result = nums[N // 2]

print(result)