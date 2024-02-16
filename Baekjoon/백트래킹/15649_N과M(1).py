def dfs(n, li):
    # 종료조건, 정답처리
    if n == M:
        res.append(li)
        return

    # 다음단계
    for i in range(1, N+1):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1, li+[i])
            v[i] = 0

N, M = map(int, input().split())
res = []
v = [0] * (N+1)  # 중복확인

dfs(0, [])
for li in res:
    print(*li)