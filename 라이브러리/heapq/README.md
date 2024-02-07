## 🧊 heapq

### ☁️ 우선순위 큐

파이썬 우선순위 큐 구현에서 heapq가 priorityQueue보다 실행시간이 적게 걸려 heapq를 일반적으로 많이 사용한다

<br>

### ☁️ 모듈 import, 함수 종류

heapq 모듈은 파이썬 내장 모듈이다

```python
from heapq import heapify, heappush, heappop
```

- heappush(heap, item)

  : item을 heap에 추가

- heappop(heap)

  : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨

- heapify(x)

  : 리스트 x를 즉각적으로 heap으로 변환함

<br>

### ☁️ 최소 힙 생성

heapq 모듈은 파이썬의 리스트를 마치 힙처럼 다룰 수 있게 도와준다

빈 리스트를 생성후 heapq 모듈 함수를 호출할 때마다 리스트에 인자로 넘기면된다

```python
heap = [] 
```

<br>

### ☁️ 힙에 원소 추가 및 삭제

heapq 모듈은 파이썬의 리스트를 마치 힙처럼 다룰 수 있게 도와준다

빈 리스트를 생성후 heapq 모듈 함수를 호출할 때마다 리스트에 인자로 넘기면된다

```python
from heapq import heappush, heappop

heap = []
heappush(heap,4)
heappush(heap,1)
heappush(heap,7)
heappush(heap,3)
print(heap)

>>>[1, 3, 7, 4]

heappop(heap)
>>> 1

print(heapq)
>>>[3,7,4] 
```

<br>

### ☁️ 최소값 삭제하지 않고 얻기

```python
print(heap[0])
>>> 3
```

<br>

### ☁️ 기존 리스트를 힙으로 변환

이미 원소가 들어있는 리스트를 힙으로 만드려면 heapyfy()라는 함수를 사용하면 된다

```python
from heapq import heapify

heap = [4,1,7,3,2,6]
heapify(heap)
print(heap)

>>> [1, 2, 6, 4, 3, 7]
```

👉 heapify() 함수에서 주의할 점은 새로운 리스트를 반환하는 것이 아니라 인자로 넘긴 리스트에 직접 변경한다

따라서 원본 리스트의 형태를 보존해야되는 경우에는 반드시 해당 리스트를 복제한 후에 인자로 넘겨야한다

<br>

### ☁️ 최소 힙

다음과 같이 최소 힙을 구현할 수 있다

```python
heap = []

# 아래 for문을 실행하고 나면 heap은 [1,2,3,5,4]로 힙 정렬이 되게 된다.
for i in range(1,6):
	heapq.heappush(heap, i)

# 작은 숫자 순서대로 1,2,3,4,5가 출력된다.
for i in range(5):
	print(heapq.heappop(heap))
```

<br>

### ☁️ 최대 힙

heapq에서는 최대 힙을 제공하지 않는다

따라서 다음과 같이 부호를 변경하는 방법을 사용해서 최대 힙을 구현한다

부호를 바꿔서 최소 힙에 넣어준 뒤에 최솟값부터 pop을 해줄 때 다시 부호를 바꿔주면 최대 힙과 동일하다

```python
heap = []
values = [1,5,3,2,4]

# 아래 for문을 실행시키고 나면 heap은 [-5,-4,-3,-1,-2]가 된다.
for value in values:
	heapq.heappush(heap, -value)

# 아래 for문을 실행시키면 5,4,3,2,1이 출력된다. 즉, 큰 숫자부터 출력이 된다.
for i in range(5):
	print(-heapq.heappop(heap))
```
