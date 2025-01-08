## 🧊 리스트 컴프리헨션

### 리스트 생성 비교

- 기존 리스트 생성코드

```python
# 1부터 3까지 정수를 순서대로 가지고 있는 리스트를 생성하는 코드
numbers = []
for n in range(1, 4):
    numbers.append(n)
>>> [1, 2, 3]
```

<br>

- 위의 코드를 리스트 컴프리헨션으로 표기

<br>

```python
[x for x in range(1, 4)]
>>> [1, 2, 3]
```
