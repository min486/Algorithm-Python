n, m = map(int, input().split())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    cnt = 0

    for a in range(i-1, x):
        for b in range(j-1, y):
            cnt += matrix[a][b]

    print(cnt)