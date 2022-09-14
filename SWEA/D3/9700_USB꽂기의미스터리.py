T = int(input())

for tc in range(1, T+1):
    p, q = map(float, input().split())

    # 뒤집어서 꽂은 후 1번 뒤집고 성공
    s1 = (1 - p) * q

    # 올바른 면이지만 실패, 2번 뒤집고 성공
    s2 = p * (1 - q) * q

    if s1 < s2:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')