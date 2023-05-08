t = 10

for tc in range(1, t+1):
    _ = input()
    n = 100
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = s3 = s4 = 0

    for i in range(n):
        s1 = s2 = 0
        for j in range(n):
            s1 += graph[i][j]
            s2 += graph[j][i]
        result = max(result, s1, s2)

        s3 += graph[i][i]
        s4 += graph[i][n-1-i]
    result = max(result, s3, s4)

    print(f'#{tc} {result}')