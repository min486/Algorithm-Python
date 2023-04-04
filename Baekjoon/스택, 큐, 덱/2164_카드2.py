from collections import deque

n = int(input())
deq = deque()

for i in range(1, n+1):
    deq.append(i)

while len(deq) > 1:
    deq.popleft()
    deq.append(deq.popleft())

print(deq[0])