## 🧊 math

> math 모듈은 수학적인 함수와 상수를 제공하는 기본 모듈
>

<br>

### ☁ math.ceil

> 주어진 숫자보다 크거나 같은 가장 작은 정수를 반환
>
> 즉, 주어진 숫자를 올림하여 정수를 반환하는 함수

<br>

``` python
import math

num1 = 3.2
result1 = math.ceil(num1)
>>> result1
4

num2 = -2.7
result2 = math.ceil(num2)
>>> result2
-1

num3 = 5
result3 = math.ceil(num3)
>>> result3
5
```

<br>

### ☁ math.floor

> 주어진 숫자보다 작거나 같은 가장 큰 정수를 반환
>
> 즉, 주어진 숫자를 내림하여 정수를 반환하는 함수

``` python
import math

num1 = 3.2
result1 = math.floor(num1)
>>> result1
3

num2 = -2.7
result2 = math.floor(num1)
>>> result2
-3

num3 = 5
result3 = math.floor(num1)
>>> result3
5
```

<br>

### ☁ 제곱근 (**0.5, math.sqrt)

> 주어진 숫자의 제곱근을 반환
>
> 양수 또는 0에 대해서만 작동하며, 음수의 제곱근은 계산할 수 없다

``` python
num1 = 9
result1 = num1 ** 0.5 or math.sqrt(num1)
>>> result1
3.0

num2 = 0
result2 = num2 ** 0.5
>>> result2
0.0

num3 = 7
result3 = num3 ** 0.5
>>> result3
2.xx
```
