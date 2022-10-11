from collections import deque

a = deque([1, 0])

if a:
    a.popleft()
    print(a)
# 결과는 deque([0])


a.append(0)
print(a)
# 결과는 deque([0, 0])

a = deque([])

if a:
    print(a)
# a가 비었으므로 출력x