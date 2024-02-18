N = int(input())

dp = [1] * 10  # dp 1차원 테이블로 구성

for _ in range(N-1):
    for j in range(1, 10):
        dp[j] += dp[j-1]

res = sum(dp)
print(res % 10007)