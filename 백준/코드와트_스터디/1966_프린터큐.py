from collections import deque

T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    q = deque([])
    li = list(map(int, input().split()))

    for j in range(len(li)):
        q.append(li[j])

    li[m] = 'result'  # 궁금한 문서의 위치
    cnt = 0
    
    while True:
        if q[0] == max(q):  # 큐의 맨 앞이 중요도 제일 높은 경우
            cnt += 1
            if li[0] == 'result':  # 리스트에서도 인덱스가 맞는 경우
                print(cnt)
                break
            else:           
                q.popleft()
                li.pop(0)
        else:               # 중요도 낮으므로, 큐의 맨 뒤로 이동
            q.append(q.popleft())
            li.append(li.pop(0))