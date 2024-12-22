## 🧊 정규표현식

### 정규표현식 re.sub()

파이썬에서 정규 표현식을 활용할 땐 re 모듈을 사용. 이 중 sub 메소드는 정규식을 이용해 문자열을 치환하는 방법이다

형식은 아래와 같다

```python
re.seb(pattern, replace, text)
> text 중 pattern에 해당하는 부분을 replace로 대체
```

<br>

### 활용 예시

```python
s = "aabbaccc"

for i in range(1, len(s)//2 + 1):
  reList = re.sub('(\w{%i})' %i, '\g<1> ', s)
  print(reList)
  
출력 (str)
> a a b b a c c c
> aa bb ac cc
> aab bac cc
> aabb accc 

for i in range(1, len(s)//2 + 1):
  reList = re.sub('(\w{%i})' %i, '\g<1> ', s).split()
  print(reList)

출력 (list)
> ['a', 'a', 'b', 'b', 'a', 'c', 'c', 'c']
> ['aa', 'bb', 'ac', 'cc']
> ['aab', 'bac', 'cc']
> ['aabb', 'accc']
```

👉 \w : 문자를 의미

👉 패턴{n} : 앞 패턴이 n번 반복해서 나타나는 경우

<br>

👉 \g : 패턴에서 괄호로 묶어놨던 하나의 group을 의미한다

그리고 <> 안의 숫자는 그게 몇 번째 group인지를 의미한다
