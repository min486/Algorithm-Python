## 🧊 클래스

### 소수

1과 자신의 수 이외의 자연수로는 나눌 수 없는 자연수

<br>

### 에라토스테네스의 체

- 효율적으로 소수를 판별할 수 있는 방법

- 입력값이 큰 경우에도 사용 가능
- 메모리/속도 둘 다 효율적이라, 일반적으로 n ≤ 10⁶ 조건에서 사용 

```python
def solution(n):
    is_prime = [False, False] + [True] * (n - 1)  # 0, 1은 소수 아님

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:  # i가 소수이면
            for j in range(i * i, n + 1, i):  # i의 배수들은 소수 아님
                is_prime[j] = False

    return sum(is_prime)

print(solution(5))  # 3 (소수: 2, 3, 5)
print(solution(10))  # 4 (소수: 2, 3, 5, 7)
```

