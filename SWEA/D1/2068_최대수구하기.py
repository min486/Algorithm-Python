t = int(input())

for tc in range(1, t+1):
    li = list(map(int, input().split()))
    result = max(li)
    
    print(f'#{tc} {result}')