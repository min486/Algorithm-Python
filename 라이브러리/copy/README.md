## 🧊 copy

### ☁ copy.deepcopy (깊은 복사)

> 깊은 복사는 내부에 객체들까지 모두 새롭게 copy 되는 것
>
> 독립적, 서로 영향 안 미침

```python
import copy

a = [[1,2],[3,4]]
b = copy.deepcopy(a)
a[1].append(5)
>>> a
[[1, 2], [3, 4, 5]]
>>> b
[[1, 2], [3, 4]]
```

<br>

### ☁ copy.copy (얕은 복사)

> 복사했지만 서로 연결되어 있는 것

```python
import copy

a = [[1,2],[3,4]]
b = copy.copy(a)
a[1].append(5)
>>> a
[[1, 2], [3, 4, 5]]
>>> b
[[1, 2], [3, 4, 5]]
```
