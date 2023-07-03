## 🧊 re

> 문자열 내 특정 패턴을 검색, 치환, 제거할 수 있는 파이썬 정규 표현식 라이브러리
>
> => 내가 작성한 정규식을 토대로 문자열 내 패턴을 감지

<br>

### ☁ re.split(pattern, string)

문자열을 패턴 기준으로 나눈다

``` python
import re

string = "50*6-3*2"
result = re.split('([-*])', string)  # 패턴 포함

>>> result
['50', '*', '6', '-', '3', '*', '2']
```

<br>

``` python
string = "50*6-3*2"
result = re.split('[-*]', string)  # 패턴 미포함

>>> result
['50', '6', '3', '2']
```

<br>

``` python
string = 'abc def*efg'
result = re.split('[ *]', string)  # 공백과 * 기준으로

>>> result
['abc', 'def', 'efg']
```
