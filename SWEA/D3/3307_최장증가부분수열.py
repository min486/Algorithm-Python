t = int(input())

for tc in range(1, t+1):
    n = int(input())
    li = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = 1

    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if li[i] > li[j]:
                dp[i] = max(dp[i], dp[j])
        dp[i] += 1

    result = max(dp)
    print(f'#{tc} {result}')