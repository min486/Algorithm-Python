n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# dp 생성 및 초기값 설정
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        # 경로가 있고, 점프 숫자가 있는 경우
        if dp[i][j] > 0 and arr[i][j] > 0:
            jump = arr[i][j]
            if j+jump < n:  # 우측 점프, 범위 이내인 경우
                dp[i][j+jump] += dp[i][j]
            if i+jump < n:  # 아래쪽 점프, 범위 이내인 경우
                dp[i+jump][j] += dp[i][j]
                
print(dp[n-1][n-1])