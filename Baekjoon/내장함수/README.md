<div align="center">
  <p>
    <img src="../README.assets/python.png">
  </p>
  <br>
  <h2>내장함수</h2>
  <p>코딩테스트 대비 내장함수 정리</p>
  <br>
  <br>
</div>



## 🧊 알파벳순 정리

> - abs
>
>   > abs(x) 는 어떤 숫자를 입력받았을 때, 그 숫자의 절댓값을 돌려주는 함수
>
>   ```python
>   >>> abs(-3)
>   3
>   >>> abs(-1.2)
>   1.2
>   ```
>
> - all
>
>   > all(x) 는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x의 요소가 모두 참이면 True,
>   >
>   > 거짓이 하나라도 있으면 False
>
>   ```python
>   >>> all([1, 2, 3])
>   True
>   >>> all([1, 2, 3, 0])
>   False
>   >>> all([])
>   True
>   ```
>
> - any
>
>   > any(x) 는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x의 요소 중 하나라도 참이 있으면 True, 
>   >
>   > x가 모두 거짓일 때에만 False 
>   >
>   > => all(x) 의 반대
>
>   ```python
>   >>> any([1, 2, 3, 0])
>   True
>   >>> any([0, ""])
>   False
>   >>> any([])
>   False
>   ```
>
> - bool
>
>   > bool() 은 참(True) / 거짓(False) 판단
>
>   - 숫자는 0이 아닌 모든 숫자는 True 이고, 0만 False
>   - 비어있는 리스트, 튜플, 딕셔너리, 문자열은 모두 False
>
>   ```python
>   '' | 빈문자열 | False
>   ' ' | 공백만 있고 비어 있는 문자열 | False
>   'abc' | 값이 있는 문자열 | True
>   [] | 빈 리스트 | False
>   [1, 2] | 값이 있는 리스트 | True
>   1 | 숫자 1 | True
>   0 | 숫자 0 | False
>   -1 | 숫자 -1 | True
>   {} | 비어있는 딕셔너리 | False
>   () | 비어있는 튜플 | False
>   ```
>
> - count
>
>   ### string.count(x, start, end)
>
>   > 문자열 내부에서 특정 문자, 혹은 문자열이 포함 되어있는지 계산해서 반환해주는 함수
>   >
>   > 리스트 내부에서 숫자, 문자도 계산
>
>   - 대소문자 구분
>   - 찾을 x 에 문자 한개를 넣어도 가능하고 문자열을 넣어도 가능
>   - start, end에 아무것도 넣지 않으면 문자열 처음부터 끝까지 탐색
>   - 찾을 x의 범위는 start <= x < end (start 포함, end 미포함)
>
>   ```python
>   a = 'ooyyy'
>   >>> a.count('y')
>   3
>
>   b = [1, 1, 1, 2, 3]
>   >>> b.count(1)
>   3
>   ```
>
> - dict
>
>   > dict() 은 키와 값으로 이루어진 딕셔너리 생성 함수
>   >
>   > 중괄호 {}도 사용 가능
>
>   - 딕셔너리 쌍 추가, 삭제
>
>   ```python
>   # 딕셔너리 쌍 추가
>   a = {1: 'a'}
>   a[2] = 'b'
>   >>> a
>   {1: 'a', 2: 'b'}
>
>   a['name'] = 'pey'
>   >>> a
>   {1: 'a', 2: 'b', 'name': 'pey'}
>
>   a[3] = [1,2]
>   >>> a
>   {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2]}
>
>   # 딕셔너리 요소 삭제
>   ## a[key]처럼 입력하면 지정한 Key에 해당하는 {key : value} 쌍이 삭제된다
>   del a[1]
>   >>> a
>   {2: 'b', 'name': 'pey', 3: [1, 2, 3]}
>   ```
>
>   - 딕셔너리에서 Key 사용해 Value 얻기
>
>   ```python
>   grade = {'pey': 10, 2:'b'}
>   >>> grade['pey']
>   10
>   >>> grade[2]
>   'b'
>   ```
>
>   - 딕셔너리 관련 함수들
>
>   ```python
>   a = {'name': 'pey', 'phone': '119', 'birth': 1118}
>
>   # Key 리스트 만들기 (keys)
>   >>> list(a.keys())
>   ['name', 'phone', 'birth']
>
>   # Value 만들기 (values)
>   >>> for i in a.values():
>           print(i)
>   pey
>   119 (str)
>   1118 (int)
>
>   # Key, Value 쌍 얻기 (items)
>   >>> a.items()
>   dict_items([('name', 'pey'), ('phone', '119'), ('birth': 1118)])
>
>   # Key: Value 쌍 모두 지우기 (clear)
>   a.clear()
>   >>> a
>   {}
>
>   # 해당 Key가 딕셔너리 안에 있는지 조사하기 (in)
>   >>> 'name' in a
>   True
>   >>> 'email' in a
>   False
>   ```
>
> - float
>
>   > float() 를 이용해서  숫자나 문자열을 실수형(Float) 으로 변환 가능
>
>    정수를 실수로 변환
>
>   ```python
>   a = 2
>   >>> float(a)
>   2.0
>   ```
>
>     문자열을 실수로 변환
>
>   ```python
>   b = '2.5'
>   >>> float(b)
>   2.5
>   ```
>
> - format
>
>   > format() 내장 함수를 이용하면 숫자를 다른 진수의 문자열로 바꿀 때 접두어(0b, 0o, ox 등)를 제외할 수 있다
>
>   ```python
>   >>> format(42, 'b') # 2진수
>   '101010'
>   >>> format(42, 'o') # 8진수
>   '52'
>   >>> format(42, 'x') # 16진수
>   '2a'
>   ```
>
> - index / find
>
>   > .index(), .find() 두 함수 모두 괄호() 안에 문자가 처음 위치한 자리의 값을 찾을 수 있다
>
>   ```python
>   a = 'hello'
>   >>> a.index('o'))
>   4
>   >>> a.find('o'))
>   4
>   ```
>
> - int
>
>   > int(x) 는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수
>
>   ```python
>   >>> int('3')
>   3
>   >>> int(3.4)
>   3
>   ```
>
> - isalpha / isdigit / isalnum
>
>    ### isalpha()
>
>    > 문자열의 구성이 알파벳 or 한글인지 확인 (문자열에 공백, 기호, 숫자가 있을시 False를 리턴)
>
>    ```python
>    ex_01 = 'A'
>    ex_02 = 'S520'
>    ex_03 = "코드앵글러"
>    ex_04 = "Code_Angler"
>    ex_05 = "Code Angler"
>
>    print(ex_01.isalpha()) # True
>    print(ex_02.isalpha()) # 숫자가 포함되여 False
>    print(ex_03.isalpha()) # True
>    print(ex_04.isalpha()) # 기호가 포함되어 False
>    print(ex_05.isalpha()) # 공백이 포함되어 False
>    ```
>
>    ### isdigit()
>
>    > 문자열의 구성이 숫자인지 확인
>
>    ```python
>    ex_01 = '123'
>    ex_02 = '010-1234-5678'
>    ex_03 = "전화번호010"
>    ex_04 = "Phone 010"
>
>    print(ex_01.isdigit()) # True
>    print(ex_02.isdigit()) # 기호가 포함되여 False
>    print(ex_03.isdigit()) # 문자가 포함되어 False
>    print(ex_04.isdigit()) # 공백이 포함되어 False
>    ```
>
>    ### isalnum()
>
>    > 문자열의 구성이 알파벳(한글) 또는 숫자인지 확인
>
>    ```python
>    ex_01 = '123'
>    ex_02 = '010-1234-5678'
>    ex_03 = "전화번호010"
>    ex_04 = "Phone 010"
>
>    print(ex_01.isalnum()) # True
>    print(ex_02.isalnum()) # 기호가 포함되여 False
>    print(ex_03.isalnum()) # True
>    print(ex_04.isalnum()) # 공백이 포함되어 False
>    ```
>
> - join
>
>   > 매개변수로 들어온 리스트나 문자열의 값과 값 사이에 구분자를 넣어서 하나의 문자열로 바꾸어 반환하는 함수
>
>    ### '구분자'. join(iterable)
>
>   ```python
>   ex = ['a', 'b', '1', '2']
>    >>> ''.join(ex)
>    ab12
>    >>> '_'.join(ex)
>    a_b_1_2
>   ```
>
> - len
>
>   > len(s) 은 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수
>
>   ```python
>   >>> len("python")
>   6
>   >>> len([1,2,3])
>   3
>   >>> len((1, 'a'))
>   2
>   ```
>
> - list
>
>   > list(s) 는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수
>
>   ```python
>   >>> list("python")
>   ['p', 'y', 't', 'h', 'o', 'n']
>   >>> list([1, 2, 3])
>   [1, 2, 3]
>   ```
>
> - append / insert
>
>   ### 리스트.append(x)
>
>   > 리스트의 끝에 x 값을 추가하는 함수
>
>   ```python
>   a = [1, 2, 3]
>   a.append(4)
>   >>> a
>   [1, 2, 3, 4]
>   ```
>
>   ### 리스트.insert(index, x)
>
>   > 리스트의 index 위치에 x 값을 추가하는 함수
>
>   ```python
>   a = [1, 2, 3]
>   a.insert(0, 0)
>   >>> a
>   [0, 1, 2, 3]
>
> - map
>
>   > map(f, iterable) 은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다
>   >
>   > map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수
>
> - max / min
>
>    ### max(iterable)
>
>   > 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수
>
>    ### min(iterable)
>
>   > 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수
>
>   ```python
>   >>> max([1, 2, 3])
>   3
>   >>> min([1, 2, 3])
>   1
>   ```
>
> - ord / chr
>
>    ### ord(c)
>
>   > 문자의 유니코드(Unicode) 값을 돌려주는 함수
>   >
>   > 문자 => 정수
>
>    ### chr(i)
>
>   > 유니코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수
>   >
>   > 정수 => 문자
>
>    a ~ z 문자와 97 ~ 122 숫자 / A ~ Z 문자와 65 ~ 90 숫자 서로 변환
>
>   ```python
>   >>> ord('a')97
>   >>> chr(97)
>   'a'
>   ```
>
> - range
>
>   - range(MAX) - 인수가 한 개
>
>     > 0 에서부터 MAX - 1까지의 숫자 연속된 객체로 만들어서 반환해주는 함수 (MAX 미포함)
>     > (0 <= x < MAX) 
>
>   - range(MIN, MAX) - 인수가 두 개
>
>     > MIN 에서부터 MAX - 1까지의 숫자를 연속된 객체로 만들어서 반환 (MAX 미포함)
>     >
>     > (MIN <= x < MAX)
>
>   - range(MIN, MAX, GAP) - 인수가 세 개일 때
>
>     > MIN에서 MAX -1까지의 숫자를 연속된 객체로 만들어 주는데, 각 숫자들 사이에 GAP 만큼의 차이를 둔다
>
>   ```python
>   >>> for i in range(3, -1, -1):
>       print(i, end=' ')
>   3 2 1 0
>   >>> range(0, 10, 2)
>   0, 2, 4, 6, 8
>   ```
>
>
> - remove / pop / clear
>
>    ### remove(value)
>
>   > 리스트에 있는 값을 이용하여 항목을 삭제
>   >
>   > 중복 값이 있을 때 제일 앞의 값만 제거
>
>   ```python
>   x = [2, 4, 6, 2, 3]
>   >>> x.remove(2)
>   [4, 6, 2, 3]
>   ```
>
>    ### pop(index)
>
>   > 원하는 인덱스 위치에 있는 요소 제거
>
>   ```python
>   x = [2, 4, 6, 2, 3]
>   >>> x.pop(2)
>   [2, 4, 2, 3]
>   ```
>
>    ### clear()
>
>   > 리스트에 저장된 모든 요소 제거
>
>   ```python
>   x = [2, 4, 6, 2, 3]
>   >>> x.clear()
>   []
>   ```
>
>
> - replace
>
>    ### str.replace('변경하고 싶은 문자', '변경 후 문자', 횟수)
>
>   > 문자열에서 변경하고 싶은 문자를 [횟수]만큼 변경하고 변경한 결과의 문자열 반환
>
>   - [횟수]를 따로 입력하지 않으면 문자열 내에서 매칭 되는 변경 문자를 모두 변경해서 반환
>   - 대소문자 구분
>
>   ```python
>   a = 'hello world'
>   >>> a.replace('hello','hi')
>   hi world
>
>   a = oxoxox
>   >>> a.replace('ox', '*', 1)
>   *oxox
>   ```
>
> - reverse / reversed
>
>   > 모두 리스트의 요소를 뒤집을 때 사용
>
>    ### [리스트].reverse()
>
>   > list 타입에서만 사용 가능
>
>   - 값을 반환하지 않는다 => 변수에 값을 담기 불가능
>
>   - 해당 리스트의 원형을 바꾼다
>
>   ```python
>   >>> B = A.reverse()
>   None
>   >>> print(A.reverse())
>   None
>   # 위의 코드들은 A라는 리스트를 모두 reverse 해준다. 
>   # 하지만 B라는 변수에 담거나 print를 바로 할 수 없다.
>   # 코드 이후에 print(A) 해야 reversed 된 값들이 나온다.
>
>   a = [1, 2, 3, 4]
>   a.reverse()
>   >>> print(a)
>   [4, 3, 2, 1]
>   ```
>
>    ### reversed([리스트])
>
>   > list 뿐만 아니라 tuple, string, dictionary 에도 사용 가능
>
>   - 객체 값을 반환한다. 반환된 값은 다시 다른 메서드를 통해 표현될 수 있다
>
>   - 해당 객체의 원형을 바꾸지 않는다
>
>   ```python
>   a = [1, 2, 3]
>   b = reversed(a)
>   >>> print(b)
>   [3, 2, 1]
>   >>> print(a)
>   [1, 2, 3]
>   ```
>
> - round
>
>   > 반올림하는 함수, 소수점을 n번째 까지만 표현, n 안적으면 반올림해서 정수로 표현
>
>    ### round(실수, n)
>
>   ```python
>   n = 0.4666
>   >>> round(n,2)
>   0.47
>   >>> round(n,3)
>   0.467
>   >>> round(n)
>   0
>
> - sort / sorted
>
>    ### .sort()
>
>   > 리스트 객체 그 자체를 정렬만 할 뿐 정렬된 결과를 돌려주지는 않는다
>
>   원형을 바꾼다
>
>   ```python
>   a = [1, 3, 2, 5, 4]
>   a.sort()
>   >>> print(a)
>   [1, 2, 3, 4, 5]
>   ```
>
>    ### sorted()
>
>   > sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수
>
>   원형을 바꾸지 않는다
>
>   ```python
>   >>> sorted([3, 1, 2])
>   [1, 2, 3]
>   >>> sorted(['a', 'c', 'b'])
>   ['a', 'b', 'c']
>   >>> sorted((3, 2, 1))
>   [1, 2, 3]
>   ```
>
>
> - set
>
>   > set() 은 집합에 관련된 것을 쉽게 처리해주고 중복을 제거해주는 함수
>
>   - 중복을 허용하지 않는다
>
>   - 순서가 없다 => 인덱싱으로 값을 얻을 수 없다
>
>   - 인덱싱으로 접근하려면 리스트 or 튜플로 변환해야 한다
>
>   - set() 하게되면 리스트가 set 타입이 되어서 {} 괄호로 묶인다
>
>   ```python
>   # 중복 제거
>   a = [1, 1, 2, 3]
>   >>> set(a)
>   {1, 2, 3}
>   >>> list(set(a))
>   [1, 2, 3]
>   
>   # | : 합집합 연산자
>   a = {1, 2, 3}
>   b = {2, 3, 4}
>   >>> a | b
>   {1, 2, 3, 4}
>   
>   # & : 교집합 연산자
>   a = {1, 2, 3}
>   b = {2, 3, 4}
>   >>> a & b
>   {2, 3}
>   
>   # - : 차집합 연산자
>   a = {1, 2, 3}
>   b = {2, 3, 4}
>   >>> a - b
>   {1}
>   
>   # 원소 추가
>   a = {1, 2, 3}
>   >>> a.add('a')
>   {1, 2, 3, 'a'}
>   
>   # 원소 삭제
>   a = {1, 2, 3}
>   >>> a.remove(2)
>   {1, 3}
>   ```
>
> - split
>
>   > split() 처럼 괄호 안에 아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다
>   >
>   > 이렇게 나눈 값은 리스트에 하나씩 들어가게 된다
>
>   ```python
>   a = "Life is too short"
>   >>> a.split()
>   ['Life', 'is', 'too', 'short']
>   ```
>
> - str
>
>   > str(object) 은 문자열 형태로 객체를 변환하여 돌려주는 함수
>
>   ```python
>   >>> str(3)
>   '3'
>   >>> str('hi')
>   'hi'
>   ```
>
> - sum
>
>   > sum(iterable) 은 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수
>
>   ```python
>   >>> sum([1,2,3])
>   6
>   >>> sum((4,5,6))
>   15
>   ```
>
> - type
>
>   > type(object) 은 입력값의 자료형이 무엇인지 알려 주는 함수
>
>   ```python
>   >>> type("abc")
>   <class 'str'>
>   >>> type([ ])
>   <class 'list'>
>   ```
>
> - upper / lower
>
>   > string.upper() 는 문자열 내부에 모든 알파벳을 대문자로 변경
>
>   > string.lower() 는 문자열 내부에 모든 알파벳을 소문자로 변경
>
>   ```python
>   str = 'Hello'
>   >>> str.upper()
>   HELLO
>   >>> str.lower()
>   hello
>   ```
>
> - isupper / islower
>
>   > string.isupper() 는 문자열 내부에 있는 모든 문자가 대문자인지 검사하는 함수
>
>   > string.islower() 는 문자열 내부에 있는 모든 문자가 소문자인지 검사하는 함수
>
>   ```python
>   str1 = 'Hello'
>   str2 = 'WORLD'
>   >>> str1.islower()
>   False
>   >>> str2.isupper()
>   True
>   ```
>
> - zip
>
>   > zip(*iterable) 은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
>
>    *iterable 은 반복 가능(iterable)한 자료형 여러 개를 입력할 수 있다는 의미
>
>   ```python
>   >>> list(zip([1, 2, 3], [4, 5, 6]))
>   [(1, 4), (2, 5), (3, 6)]
>   >>> list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
>   [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
>   >>> list(zip("abc", "def"))
>   [('a', 'd'), ('b', 'e'), ('c', 'f')]
>   ```
>

