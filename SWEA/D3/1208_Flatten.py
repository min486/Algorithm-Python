t = 10 

for tc in range(1, t+1):
    n = int(input())
    li = list(map(int, input().split()))
    
    for _ in range(n):
        li.sort()
        if max(li) - min(li) == 0 or max(li) - min(li) == 1:
            break
        li[0] += 1
        li[-1] -= 1
        
    print(f'#{tc} {max(li) - min(li)}')