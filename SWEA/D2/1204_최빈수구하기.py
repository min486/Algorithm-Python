T  = int(input())

for tc in range(1, T+1):
    tc_num = input()
    scores = list(map(int, input().split()))
    cnt = [0] * 101
    
    max_cnt = 0
    many_num = 0
    
    for i in scores:
        cnt[i] += 1
    for x in range(1, len(cnt)):
        # 빈도값이 같으면 큰 수를 출력
        if cnt[x] >= max_cnt:
            max_cnt = cnt[x]
            many_num = x
            
    print(f'#{tc_num} {many_num}')