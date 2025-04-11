def solution(s):
    small = s.lower()
    p_cnt = small.count('p')
    y_cnt = small.count('y')
    
    if p_cnt == y_cnt == 0:
        return True
    else:
        if p_cnt == y_cnt:
            return True
        else:
            return False