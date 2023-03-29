from collections import deque

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    q = deque()

    for i in range(len(li)):
        q.append(li[i])

    li[m] = 'result'  # 구하고자 하는 문서의 위치
    cnt = 0
    
    while True:
        # 첫번째 문서 중요도가 제일 높으면 
        if q[0] == max(q):
            cnt += 1
            if li[0] == 'result':
                print(cnt)
                break
            else: 
                q.popleft()
                li.pop(0)
        # 제일 높지 않으면 가장 뒤에 재배치
        else:
            q.append(q.popleft())
            li.append(li.pop(0))