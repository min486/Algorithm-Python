def dfs(now, visit):
    global result
    result = max(result, len(visit))  # 최대값 갱신

    for n in graph[now]:  # now와 연결된 정점 하나씩 처리
        if n not in visit:  # 방문하지 않은 정점인 경우
            dfs(n, visit+[n])

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    result = 0
    for s in range(1, n+1):
        dfs(s, [s])
    print(f'#{tc} {result}')