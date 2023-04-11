## 🧊 itertools.permutations

> 순서를 생각하며 카드 뽑을 때 사용
>
> itertools.permutations(iterable, r)은 반복 가능 객체 중에서 r개를 선택한 순열을 반환하는 함수

<br>

### ☁ 문제

1, 2, 3 숫자가 적힌 3장의 카드에서 두 장의 카드를 꺼내 만들 수 있는 2자리 숫자를 모두 구하려면?

<br>

### ☁ 풀이 (순열)

[1, 2, 3] 3장의 카드 중 순서에 상관없이 2장을 뽑는 경우의 수는 모두 3가지이다 (조합)

- 1, 2
- 2, 3
- 1, 3

하지만, 이 문제에서는 2자리 숫자이므로 이 3가지에 순서를 더해 다음처럼 6가지가 된다 (순열)

- 1, 2
- 2, 1
- 2, 3
- 3, 2
- 1, 3
- 3, 1

이 순열은 itertools.permutations()를 사용하면 간단히 구할 수 있다

``` python
from itertools import permutations
list(permutations(['1', '2', '3'], 2))
>>> [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
```

<br>

### ☁ 조합

> 순서를 생각하지 않고 카드 뽑을 때 사용
>
> 3장의 카드에서 순서에 상관없이 2장을 고르는 조합은 itertools.combinations()를 사용

``` python
from itertools import combinations
list(combinations(['1', '2', '3'], 2))
>>> [('1', '2'), ('1', '3'), ('2', '3')]
```
