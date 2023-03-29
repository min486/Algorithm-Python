## 🧊 DFS (깊이우선탐색, Depth-First Search)

> 시작 정점으로부터 갈 수 있는 하위 정점까지 가장 깊게 탐색 하고 ,
> 더 이상 갈 곳이 없다면 마지막 갈림길로 돌아와서 다른 정점을 탐색하며 결국 모든 정점을 방문하는 순회 방법

<br>

### ☁ 반복문을 이용한 DFS

> DFS는 직전에 방문한 정점으로 차례로 돌아가야 하므로 , 후입선출(LIFO) 구조의 스택을 사용한다

#### 예제 입력

```python
7
6
1 2
2 3
1 5
5 2
5 6
4 7
```

#### 인접 리스트 만들기

```python
n = int(input())  # 정점 개수
m = int(input())  # 간선 개수
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
total = 0

# 인접 리스트 만들기
for _ in range(m):
    v1, v2 = map(int, input().split())
	graph[v1].append(v2)
	graph[v2].append(v1)
```

#### 인접 리스트 생성 결과

```python
graph = [
    [],
    [2, 5],
    [1, 3, 5],
    [2], 
    [7],
    [1, 2, 6],
    [5],
    [4]
]
```

#### DFS 진행

```python
visited = [False] * n  # 방문 처리 리스트 만들기

def dfs(start):
	stack = [start]  # 돌아갈 곳을 기록
	visited[start] = True  # 시작 정점 방문 처리

    while stack:  # 스택이 빌 때까지 (돌아갈 곳이 없을때까지) 반복
	cur = stack.pop()  # 현재 방문 정점 (후입선출)

    for adj in graph[cur]:  # 인접한 모든 정점에 대해
		if not visited[adj]: # 아직 방문하지 않았다면
			visited[adj] = True  # 방문 처리
			stack.append(adj)  # 스택에 넣기

dfs(1)  # 1번 정점에서 시작
```
