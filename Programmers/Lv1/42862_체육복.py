def solution(n, lost, reserve):
    # 여벌 있는 학생이 도난당한 경우가 있으므로, 각 배열에서 제외시킨다
    re_only = set(reserve) - set(lost)
    lo_only = set(lost) - set(reserve)

    # 체육복 빌려주기
    for i in re_only:
        front = i-1
        back = i+1
        if front in lo_only:
            lo_only.remove(front)
        elif back in lo_only:
            lo_only.remove(back)
    
    # 학생 수 계산
    ans = n - len(lo_only)
    return ans