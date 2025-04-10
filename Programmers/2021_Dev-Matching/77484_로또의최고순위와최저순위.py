def solution(lottos, win_nums):
    # 순위:당첨개수 해시테이블
    dct = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    # 당첨개수, 0개수 카운팅
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
            
    zero_cnt = lottos.count(0)
    
    # 최고순위/최저순위 구하기
    max_num = dct[cnt+zero_cnt]
    min_num = dct[cnt]
    
    return [max_num, min_num]