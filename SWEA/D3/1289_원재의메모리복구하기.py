t = int(input())

for tc in range(1, t+1):
    li = list(map(int, input()))
    cnt = li[0]
    
    for i in range(1, len(li)):
        if li[i] != li[i-1]:
            cnt += 1
            
    print(f'#{tc} {cnt}')