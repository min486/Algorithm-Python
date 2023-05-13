t = int(input())

for tc in range(1, t+1):
    a, b = map(int, input().split())
    
    if a > b:
        result = '>'
    elif a < b:
        result = '<'
    elif a == b:
        result = '='
    
    print(f'#{tc} {result}')