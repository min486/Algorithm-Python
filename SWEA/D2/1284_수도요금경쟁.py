T = int(input())

for tc in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    a_fee = W * P

    if W <= R:
        b_fee = Q
    else: 
        b_fee = Q + (W - R) * S

    print(f'#{tc} {min(a_fee, b_fee)}')
