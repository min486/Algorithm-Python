t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    
    li.sort(reverse=True)
    result = sum(li[:k])
    
    print(f'#{tc} {result}')