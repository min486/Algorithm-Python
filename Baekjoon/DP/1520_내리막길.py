def dfs(ci,cj):
    if dp[ci][cj] == -1:
        dp[ci][cj] = 0
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            pi, pj = ci+di, cj+dj
            if arr[pi][pj] > arr[ci][cj]:
                dp[ci][cj] += dfs(pi,pj)
    return dp[ci][cj]

N, M = map(int, input().split())
arr = [[0]*(M+2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(M+2)]

dp = [[-1]*(M+2) for _ in range(N+2)]
dp[1][1] = 1

print(dfs(N,M))