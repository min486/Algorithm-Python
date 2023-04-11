t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    result = 0
    for _ in range(n) :
        p, x = map(float, input().split())
        result += p * x

    # f-string을 사용하여 소수점 지정
    print(f'#{tc} {result:.6f}')