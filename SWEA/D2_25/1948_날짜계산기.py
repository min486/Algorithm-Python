li = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

t = int(input())

for tc in range(1, t+1):
    m1, d1, m2, d2 = map(int, input().split())

    if m1 == m2:
        ans = d2-d1+1
    else:
        ans = li[m1]-d1+1
        for i in range(m1+1, m2):
            ans += li[i]
        ans += d2

    print(f'#{tc} {ans}')