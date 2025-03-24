from collections import deque

def bfs(s):
    q = []
    v = [0]*101

    q.append(s)
    v[s] = 1
    ans = s

    while q:
        c = q.popleft()

        if v[ans]<v[c] or (v[ans]==v[c] and ans<c):
            ans = c

        for n in adj[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = v[c]+1
    return ans

t = 10
for tc in range(1, t+1):
    n, s = map(int, input().split())
    li = list(map(int, input().split()))

    adj = [[] for _ in range(101)]
    for i in range(0, len(li), 2):
        p, c = li[i], li[i+1]
        adj[p].append(c)

    ans = bfs(s)
    print(f'#{tc} {ans}')