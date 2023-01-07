n, x = map(int, input().split())
nums = list(map(int, input().split()))

for i in nums:
    if i < x:
        print(i, end=' ')