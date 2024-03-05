from collections import deque

def solution(rc, operations):
    rc = deque([deque(li) for li in rc])
    firsts = deque()
    lasts = deque()
    
    # firsts / rc / lasts 분리
    for q in rc:
        firsts.append(q.popleft())
        lasts.append(q.pop())
    
    for ope in operations:
        if ope == 'ShiftRow':
            rc.appendleft(rc.pop())
            firsts.appendleft(firsts.pop())
            lasts.appendleft(lasts.pop())
        else:  # Rotate
            rc[0].appendleft(firsts.popleft())
            lasts.appendleft(rc[0].pop())
            rc[-1].append(lasts.pop())
            firsts.append(rc[-1].popleft())
            
    # firsts / rc / lasts 합치기
    for q in rc:  
        q.appendleft(firsts.popleft())
        q.append(lasts.popleft())
    
    res = [list(q) for q in rc]
    return res