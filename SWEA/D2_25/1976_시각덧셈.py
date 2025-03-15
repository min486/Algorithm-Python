t = int(input())

for tc in range(1, t+1):
    h1, m1, h2, m2 = map(int, input().split())
    total_h = h1 + h2
    total_m = m1 + m2

    if m1 + m2 > 59:
        total_m -= 60
        total_h += 1

    if h1 + h2 > 12:
        total_h -= 12

    print(f'#{tc} {total_h} {total_m}')