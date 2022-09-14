T = int(input())

for tc in range(1, T+1):
    n, a, b = map(int, input().split())
    min_value = 0

    if n < a + b:
        min_value = (a + b) - n
    max_value = min(a, b)

    print(f'#{tc} {max_value} {min_value}')