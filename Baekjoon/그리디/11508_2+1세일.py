n = int(input())
li = []

for _ in range(n):
    li.append(int(input()))

# 최대한 비싼가격을 빼기위해 내림차순 정렬
li.sort(reverse = True)
three = 0
    
# range의 세번째 인수로 간격 설정
for i in range(2, len(li), 3):
    three += li[i]

# 전체 수의 합 - 세번째 수들의 합
print(sum(li) - three)