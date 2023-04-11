T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    info = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int,input().split())
        info[x].append(y)
        info[y].append(x)

    res = 0
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            for k in range(j+1,N+1):
                if i in info[j] and j in info[k] and k in info[i]:
                    res += 1

    print("#{} {}".format(t,res))