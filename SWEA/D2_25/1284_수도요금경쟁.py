t = int(input())

for tc in range(1, t+1):
    p, q, r, s, w = map(int, input().split())

    a_fee = w * p

    if w <= r:
        b_fee = q
    else:
        b_fee = q + (w-r) * s

    answer = min(a_fee, b_fee)

    print(f'#{tc} {answer}')