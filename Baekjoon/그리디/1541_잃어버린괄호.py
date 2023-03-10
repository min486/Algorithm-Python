# -로 구분하여 나누기
# -가 시작되면 다음 -가 나오기전까지 숫자들 묶어줘서 가장 큰 수를 빼기 위해
minus = input().split('-') 
li = []

for i in minus:  # 나눈 문자열 순회
    cnt = 0 
    plus = i.split('+')  # +로 나누기

    for j in plus:  # +로 나눈 문자열 순회
        cnt += int(j) 
    li.append(cnt)  # 계산한 숫자 리스트에 넣기

result = li[0]  # 첫 숫자에서 빼기 위해서 첫 숫자로 초기화

for i in range(1, len(li)):
    result -= li[i]  # 묶어준 숫자 빼주기
print(result)