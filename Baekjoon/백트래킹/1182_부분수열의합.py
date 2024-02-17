def dfs(n, sm, cnt):
    global res

    if n == N:
        if sm == S and cnt > 0:
            res += 1
        return

    # 다음단계
    dfs(n+1, sm+li[n], cnt+1)  # 포함하는 경우
    dfs(n+1, sm, cnt)  # 포함하지 않는 경우

N, S = map(int, input().split())
li = list(map(int, input().split()))

res = 0
dfs(0, 0, 0)  # 인덱스 0부터, 전체 합, 포함한 개수>0인지 체크
print(res)