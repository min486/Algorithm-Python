import math

T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B+1):
        if str(i) == str(i)[::-1]:
            value = math.sqrt(i)
            if value == int(value) and str(int(value)) == str(int(value))[::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')