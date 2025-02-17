from collections import deque

n, k = map(int, input().split())
deq = deque()
result = []

for i in range(1, n+1):
    deq.append(i)

while deq:
    for _ in range(k-1):
        deq.append(deq.popleft())

    result.append(deq.popleft())

print(str(result).replace('[', '<').replace(']', '>'))