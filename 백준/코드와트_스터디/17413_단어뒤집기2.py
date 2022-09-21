result = ''
word = ''
tag = False  # 태그는 result에, 단어는 word에 넣기위해 사용

string = input()

for i in string:
    if i == '<':
        tag = True
        result += word[::-1]  # 뒤쪽 태그에서 바로 앞에 단어 뒤집기
        word = ''
        result += i
        continue
    
    elif i == '>':
        tag = False
        result += i
        continue

    elif i == ' ':                  # 단어사이 공백일 때,
        result += word[::-1] + ' '  # 앞에 단어 뒤집어서 result에 추가
        word = ''
        continue

    if tag:  # 태그 속 문자들
        result += i
    else:  # 단어의 문자들
        word += i

print(result + word[::-1])
