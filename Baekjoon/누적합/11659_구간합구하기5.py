import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n+1)]
p_sum = [[0] * (n+1) for _ in range(n+1)]

for _ in range(n):
    graph.append([0] + [int(x) for x in input().split()])

for i in range(1, n+1):
    for j in range(1 , n+1):
        p_sum[i][j] = p_sum[i-1][j] + p_sum[i][j-1] - p_sum[i-1][j-1] + graph[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = p_sum[x2][y2] - p_sum[x1-1][y2] - p_sum[x2][y1-1] + p_sum[x1-1][y1-1]

    print(result)