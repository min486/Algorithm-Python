t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    check = [0] * (n+1)
    
    for i in li:
        check[i] = 1
        
    result = []
    for i in range(1, n+1):
        if check[i] == 0:
            result.append(i)
        
    print(f'#{tc}', *result)