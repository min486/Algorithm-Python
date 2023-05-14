t = int(input())

for tc in range(1, t+1):
    l, u, x = map(int, input().split())
    
    if l <= x <= u:
        result = 0
    elif u < x:
        result = -1
    else:
        result = l-x

    print(f'#{tc} {result}')