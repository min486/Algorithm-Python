t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    m = n // 2
    s = e = m
    result = 0
    
    for i in range(n):
        for j in range(s, e+1):
            result += arr[i][j]
        if i < m:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
            
    print(f'#{tc} {result}')