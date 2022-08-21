T = int(input())
 
for tc in range(1, T + 1):
    ten = list(map(int, input().split()))
     
    total = 0
    for i in ten:
        total += i
    result = round(total / 10)
     
    print(f'#{tc} {result}')