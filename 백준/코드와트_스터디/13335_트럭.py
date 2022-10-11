from collections import deque

n, w, L = map(int, input().split())
q = deque(list(map(int, input().split())))  # 트럭들의 무게들

bridge = deque([0] * w)  # deque([0, 0])
cnt = 0

while bridge:  # 다리에서 마지막 트럭이 나갈때까지
    cnt += 1
    bridge.popleft()
    if q:  # 트럭이 있는 경우
        if sum(bridge) + q[0] <= L:  # 트럭들 무게의 합 <= 최대하중
            bridge.append(q.popleft())
        else:
            bridge.append(0)  # 다리 공간 채워주기

print(cnt)