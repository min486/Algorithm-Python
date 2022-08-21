T = int(input())
 
for tc in range(1, T + 1):
    ten = list(map(int, input().split()))
     
    result = 0
    for i in ten:
        if i % 2 == 1:
            result += i
             
    print(f'#{tc} {result}')