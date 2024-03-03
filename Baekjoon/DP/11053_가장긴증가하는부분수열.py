N = int(input())
li = [0] + list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(1, N+1):
    mx = 0
    for j in range(i):  # 0 ~ i-1 중에서 max값
        if li[i] > li[j]:
            mx = max(mx, dp[j])
    dp[i] = mx + 1

print(max(dp))