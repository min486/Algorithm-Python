T = int(input())
 
for tc in range(1, T + 1):
    a, b = map(int, input().split())
    div = a // b
    rem = a % b
     
    print(f'#{tc} {div} {rem}')