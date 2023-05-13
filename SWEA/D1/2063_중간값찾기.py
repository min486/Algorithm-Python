n = int(input())
nums = list(map(int, input().split()))

nums.sort()
result = nums[n//2]

print(result)