t = 10

for tc in range(1, t+1):
    _ = input()
    n, m = map(int, input().split())

    print(f'#{tc} {n**m}')