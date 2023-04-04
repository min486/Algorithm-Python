from collections import deque

n, w, l = map(int, input().split())
deq = deque(map(int, input().split()))

bridge = deque([0] * w)
cnt = 0

while bridge:
    cnt += 1
    bridge.popleft()

    if deq:
        if sum(bridge) + deq[0] <= l:
            bridge.append(deq.popleft())
        else:
            bridge.append(0)

print(cnt)