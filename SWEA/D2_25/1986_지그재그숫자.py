t = int(input())

for tc in range(1, t+1):
    n = int(input())
    ans = 0

    for i in range(1, n+1):
        if i % 2 == 1:
            ans += i
        else:
            ans -= i

    print(f'#{tc} {ans}')