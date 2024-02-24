N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# dp 생성 및 초기값 설정
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        # 경로가 있고, 점프 숫자가 있으면
        if dp[i][j] > 0 and arr[i][j] > 0:
            jump = arr[i][j]
            if j+jump < N:  
                dp[i][j+jump] += dp[i][j]  # 오른쪽 점프
            if i+jump < N:
                dp[i+jump][j] += dp[i][j]  # 아래 점프

print(dp[N-1][N-1])