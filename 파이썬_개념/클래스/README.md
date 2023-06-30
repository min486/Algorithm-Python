## 🧊 클래스

### ☁ 클래스와 객체

- 클래스(class) : 똑같은 무언가를 계속 만들어 낼 수 있는 설계 도면(붕어빵 틀)
- 객체(object) : 클래스로 만든 것(붕어빵 틀로 만든 붕어빵)
- 클래스 특징 : 객체마다 고유한 성격을 가진다. 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않는다

<br>

### ☁ 클래스 사용 예시

계산기 프로그램 (더하기 기능)

```python
# 한 프로그램에서 2대의 계산기가 필요한 상황 
# 각 계산기는 각각의 결과값을 유지해야 하므로 함수를 따로 만들어야 한다

result1 = 0
result2 = 0

def add1(num):  # 계산기1
    global result1
    result1 += num
    return result1

def add2(num):  # 계산기2
    global result2
    result2 += num
    return result2

print(add1(3))  # 3
print(add1(4))  # 7
print(add2(3))  # 3
print(add2(7))  # 10
```

하지만 계산기가 3개, 5개, 10개로 점점 더 많이 필요해지면?

계산기마다 빼기나 곱하기와 같은 기능을 추가해야 한다면?

=> 상황은 점점 더 어려워진다

<br>

위와 같은 경우, 클래스를 사용하면 간단하게 해결할 수 있다

```python
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))  # 3
print(cal1.add(4))  # 7
print(cal2.add(3))  # 3
print(cal2.add(7))  # 10
```
