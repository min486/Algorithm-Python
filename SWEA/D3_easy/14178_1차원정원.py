t = int(input())

for tc in range(1, t+1) :
    n, d = map(int, input().split())
    d = d * 2 + 1  # 분무기 1개로 뿌릴 수 있는 꽃의 개수
    result = n // d

    if n % d != 0:
        result += 1

    print(f'#{tc} {result}')