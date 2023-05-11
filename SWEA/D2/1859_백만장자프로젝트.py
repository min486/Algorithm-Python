t = int(input())

for tc in range(1, t+1):
    n = int(input())
    li = list(map(int, input().split()))[::-1]
    result = mx = 0

    for i in li:
        if mx < i:
            mx = i
        else:
            result += (mx-i)

    print(f'#{tc} {result}')