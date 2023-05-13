t = int(input())

for tc in range(1, t+1):
    li = list(map(int, input().split()))
    sm = 0
    
    for i in li:
        sm += i
    result = round(sm/10)

    print(f'#{tc} {result}')