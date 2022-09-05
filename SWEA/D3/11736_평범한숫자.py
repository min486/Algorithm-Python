T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    cnt = 0
    
    for p in range(1, N-1):
        max_value = max(li[p-1], li[p], li[p+1])
        min_value = min(li[p-1], li[p], li[p+1])

        if li[p] != max_value and li[p] != min_value:
            cnt += 1
        else:
            continue
            
    print(f'#{tc} {cnt}')