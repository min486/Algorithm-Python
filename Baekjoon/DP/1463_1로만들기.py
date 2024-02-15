N = int(input())

dp = [0] * (N+1)  # dp[1]=0 초기값 설정

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:  # 숫자가 2의 배수인 경우 (*2)
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

res = dp[N]
print(res)