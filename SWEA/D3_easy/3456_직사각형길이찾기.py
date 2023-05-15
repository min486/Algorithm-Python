t = int(input())

for tc in range(1, t+1):
    li = list(map(int, input().split()))
    li.sort()
    result = li[0] + li[2] - li[1]
    
    print(f'#{tc} {result}')