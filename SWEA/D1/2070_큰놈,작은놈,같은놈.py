T = int(input())
 
for tc in range(1, T + 1):
    li = list(map(int, input().split()))
     
    if li[0] > li[1]:
        result = '>'
    if li[0] < li[1]:
        result = '<'
    if li[0] == li[1]:
        result = '='
         
    print(f'#{tc} {result}')