def solution(nums):
    # 폰켓몬 종류 수
    cnt = len(set(nums))
    # 가질 수 있는 수 (N/2 마리)    
    get_cnt = len(nums) // 2
    
    return min(cnt, get_cnt)