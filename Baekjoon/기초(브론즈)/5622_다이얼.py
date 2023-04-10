alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
min_time = 0

# 문자열의 길이만큼 반복되는 for문
for i in range(len(word)):
    # 문자열 앞부터 하나씩 alpha에 있는지 체크
    for j in alpha:
        # 만약 있을 경우 인덱스+3초 걸리므로 조건 설정
        if word[i] in j:
            min_time += alpha.index(j) + 3

print(min_time)