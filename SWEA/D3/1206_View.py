t = 10

for tc in range(1, t+1):
    n = int(input())
    li = list(map(int, input().split()))
    result = 0
    
    for i in range(2, n-2):
        mx = max(li[i-2 : i] + li[i+1 : i+3])
        if li[i] > mx:
            result += li[i] - mx

    print(f'#{tc} {result}')