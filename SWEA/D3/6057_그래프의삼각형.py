t = int(input())

for tc in range(1, t+1):
    n, m = map(int,input().split())
    info = [[] for _ in range(n+1)]

    for _ in range(m):
        x, y = map(int,input().split())
        info[x].append(y)
        info[y].append(x)

    result = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                if i in info[j] and j in info[k] and k in info[i]:
                    result += 1

    print(f'#{tc} {result}')