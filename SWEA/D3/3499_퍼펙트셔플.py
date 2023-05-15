t = int(input())

for tc in range(1, t+1):
    n = int(input())
    li = input().split()
    
    if n % 2 == 0:
        div = n//2
        ps1 = li[:div]
        ps2 = li[div:]
    else:
        div = n//2+1
        ps1 = li[:div]
        ps2 = li[div:]

    result = []
    while ps1:
        result.append(ps1.pop(0))
        if ps2:
            result.append(ps2.pop(0))

    print(f'#{tc}', *result)