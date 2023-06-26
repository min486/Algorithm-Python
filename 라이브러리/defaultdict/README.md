## 🧊 collections.defaultdict

> dictionary에 기본값을 정의하고 키값이 없더라고 에러를 출력하지 않고 기본값 출력

- 기존 dictionary에서 없는 key를 접근 or 조작할 때 KeyError 발생

  => 이를 보완한 것이 defaultdict

- defaultdict에서는 없는 key를 접근 or 조작할 때 key 값이 없다면 defaultdict 쪽에서 key를 만들고 default 값을 자체적으로 생성

  => dictionary의 missing key 문제를 해결해준다

- defaultdict에 인자 값은 list, set, int 받을 수 있다

<br>

### ☁ defaultdict(list)

각 부서별 값에는 default값이 들어가있다가 append로 각 값들을 초기화시켜주니 부서별 사원이름이 나온다

``` python
from collections import defaultdict

li = [('영업부', '서린'),
      ('영업부', '조인'),
      ('회계부', '민기'),
      ('마케팅부', '유엔'),
      ('마케팅부', '소다')]

dic = defaultdict(list)
for department, employee in li:
    dic[department].append(employee)
    
>>> dic
defaultdict(<class 'list'>, {'영업부': ['서린', '조인'], '회계부': ['민기'], '마케팅부': ['유엔', '소다']})
```

<br>

### ☁ defaultdict(set)

중복되는 값이 있을 때 set을 이용하면 중복되는 아이템이 없게 설정할 수 있다

``` python
from collections import defaultdict

li = [('영업부', '서린'),
      ('영업부', '조인'),
      ('회계부', '민기'),
      ('회계부', '민기'),
      ('영업부', '조인')]

dic = defaultdict(list)
for department, employee in li:
    dic[department].add(employee)
    
>>> dic
defaultdict(<class 'set'>, {'영업부': {'서린', '조인'}, '회계부': {'민기'}})
```

<br>

### ☁ defaultdict(int)

> defaultdict 안에 있는 각 key 안의 개수 세기

defaultdict을 int로 설정할 경우 리턴값은 0이며 이를 활용해 각 부서의 사원수를 셀 수 있다

대신 이 코드를 실행할 때에는 데이터의 중복값이 없어야한다. 있을 경우 다 포함되서 나온다

``` python
from collections import defaultdict

li = [('영업부', '영업사원1'),
      ('영업부', '영업사원2'),
      ('회계부', '회계사원1'),
      ('회계부', '회계사원2'),
      ('마케팅부', '마케팅사원1'),
      ('영업부', '영업사원3')]

dic = defaultdict(int)
for department, _ in li:
    dic[department] += 1
    
>>> dic
defaultdict(<class 'int'>, {'영업부': 3, '회계부': 2, '마케팅부': 1})
```
