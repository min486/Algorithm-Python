import math

T = int(input())

for tc in range(1, T+1):
    N, D = map(int, input().split())
    section = D * 2 + 1
    result = math.ceil(N / section)

    print(f'#{tc} {result}')