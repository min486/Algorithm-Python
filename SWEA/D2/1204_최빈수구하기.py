t = int(input())

for tc in range(1, t+1):
    _ = input()
    li = list(map(int, input().split()))
    cnt = [0] * 101
    many_cnt = 0
    result = 0

    for i in li:
        cnt[i] += 1
        
    # 최빈수가 같으면 큰 수 출력    
    for j in range(len(cnt)):
        if cnt[j] >= many_cnt:  
            many_cnt = cnt[j]
            result = j
            
    print(f'#{tc} {result}')