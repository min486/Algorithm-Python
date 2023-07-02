score_diff = 0  # 라이언 점수 - 어피치 점수  
answer = [0] * 11

def calculate_score_diff(rinfo, ainfo):
    rscore = ascore = 0
    for i, (r, a) in enumerate(zip(rinfo, ainfo)):
        if r == a == 0:
            continue
        if r > a:
            rscore += 10 - i
        else:
            ascore += 10 - i
    return rscore - ascore

def better(info1, info2):
    for i1, i2 in zip(reversed(info1), reversed(info2)):
        if i1 > i2:
            return True
        elif i1 < i2:
            return False
    return False

def search(idx, n, rinfo, ainfo):
    global score_diff
    global answer
    if idx == 10 or n == 0:
        rinfo[-1] = n
        diff = calculate_score_diff(rinfo, ainfo)
        if diff > score_diff:
            score_diff = diff
            answer = rinfo[:]
        elif diff == score_diff and better(rinfo, answer):
            answer = rinfo[:]
        return
    
    # 라이언이 어피치보다 화살 한개 더 쏘는 경우
    if n > ainfo[idx]:
        rinfo[idx] = ainfo[idx] + 1
        search(idx + 1, n - rinfo[idx], rinfo, ainfo)
        rinfo[idx] = 0
    
    # 해당 idx에 화살을 안 쏘는 경우
    search(idx + 1, n, rinfo, ainfo)

def solution(n, info):
    search(0, n, [0]*11, info)
    if score_diff <= 0:  # 라이언이 지거나 비긴 경우
        return [-1]
    return answer