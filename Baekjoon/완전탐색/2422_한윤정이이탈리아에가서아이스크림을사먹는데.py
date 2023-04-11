n, m = map(int, input().split())
ice = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    ice[a][b] = 1
    ice[b][a] = 1

result = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        for k in range(j+1, n+1):
            if (ice[i][j] == 0) and (ice[j][k] == 0) and (ice[k][i] == 0):
                result += 1
                
print(result)