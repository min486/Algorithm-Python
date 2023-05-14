t = int(input())

for tc in range(1, t+1):
    n, q = map(int, input().split())
    check = [0] * (n+1)

    for i in range(1, q+1):
        l, r = map(int, input().split())
        for j in range(l, r+1):
            check[j] = i

    check.pop(0)
    print(f'#{tc}', *check)