## 🧊 queue.PriorityQueue

> 우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조

- 각 원소들이 우선순위를 가지고 있다

- 우선순위 큐는 힙(heap)이라는 자료구조를 통해 구현할 수 있다


<br>

### ☁ PriorityQueue

``` python
from queue import PriorityQueue

pq = PriorityQueue() 
pq2 = PriorityQueue(maxsize=10)  # maxsize를 활용하면 크기 제한 가능
```

<br>

### ☁ put

하나의 원소를 우선순위를 지정하여 추가하는 함수

``` python
# 원소를 넣는 과정
pq.put(3)  
pq.put(4)
pq.put(1)

pq2.put((1, 'apple'))  # (우선순위, 값)의 형태로 저장할 수도 있음
```

<br>

### ☁ get

가장 높은 우선순위를 가진 원소를 큐에서 제거하고 반환하는 함수

``` python
# 원소 삭제 및 반환
pq.get()  # 1

pq2.get()[1]  # (우선순위, 값)의 형태에서 값 반환
```
