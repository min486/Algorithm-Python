from itertools import combinations

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    cnt = 0

    for i in range(1, n+1):
        for com in combinations(li, i):
            if sum(com) == k:
                cnt += 1

    print(f'#{tc} {cnt}')