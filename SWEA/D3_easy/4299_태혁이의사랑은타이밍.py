t = int(input())

for tc in range(1, t+1):
    d, h, m = map(int, input().split())
    time = 11*24*60 + 11*60 + 11
    time_sad = d*24*60 + h*60 + m
    result = time_sad - time

    if result < 0:
        result = -1
        
    print(f'#{tc} {result}')