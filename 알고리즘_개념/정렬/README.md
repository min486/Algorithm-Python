## 🧊 정렬

### ☁ key=lambda

> 내가 원하는 기준으로 정렬시 사용

<br>

#### key 하나일 때

- ex 1)

  ```python
  li = ['abc', 'bac', 'bca']
  sorted(li, key=lambda x : x[0])
  ```

  👉 li에 속하는 각 원소들을 x라고 생각했을 때, x[0] 기준으로 정렬하기

- ex 2)

  ```python
  li = [12, 14, 23, 24, 16]
  li_idx = sorted(range(len(li)), key=lambda k : li[k]) 
  
  # li_idx는 [0, 1, 4, 2, 3]
  ```

  👉 리스트 내 원소를 크기순으로 정렬했을 때의 인덱스 구하기

<br>

#### key 여러개일 때

- ex 1)

  ```python
  arr = ['abb', 'acc', 'bcd']
  sorted(arr, key=lambda x : (x[0], x[1]))
  ```

  👉 x[0] 기준으로 정렬하고, 같을 경우 x[1] 기준으로 정렬하기

- ex 2)

  ```python
  arr = ['abb', 'acc', 'bcd']
  sorted(arr, key=lambda x : (-x[0], x[1]))
  ```

  👉 x[0]는 내림차순, x[1]는 오름차순을 기준으로 정렬하기
