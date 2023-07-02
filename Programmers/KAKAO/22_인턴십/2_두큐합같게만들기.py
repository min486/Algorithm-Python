from collections import deque

def solution(queue1, queue2):
    n = len(queue1)
    total1, total2 = sum(queue1), sum(queue2)
    q1, q2 = deque(queue1), deque(queue2)
    
    for i in range(n * 3):  # 두 큐의 모든 원소를 바꾸려면 (길이*2) 횟수이므로 넉넉히 *3으로
        if total1 == total2:
            return i
        if total1 < total2:
            x = q2.popleft()
            total1 += x
            total2 -= x
            q1.append(x)
        else:
            x = q1.popleft()
            total2 += x
            total1 -= x
            q2.append(x)
    
    return -1