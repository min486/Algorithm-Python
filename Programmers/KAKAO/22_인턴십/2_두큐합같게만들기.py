from collections import deque

def solution(queue1, queue2):
    s1 = sum(queue1)
    s2 = sum(queue2)

    if (s1+s2) % 2:
        return -1

    queue1 = deque(queue1)  # 14
    queue2 = deque(queue2)  # 16
    le = len(queue1)
    cnt = 0

    while cnt < 4*le :
        if s1 == s2:
            return cnt
        elif s1 > s2:
            ele = queue1.popleft()
            s1 -= ele
            queue2.append(ele)
            s2 += ele
        else:
            ele = queue2.popleft()
            s2 -= ele
            queue1.append(ele)
            s1 += ele
        cnt += 1
    return -1