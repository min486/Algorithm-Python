n = int(input())
li = []

for _ in range(n):
    a = int(input())
    li.append(a)

li.sort()  # 입력받은 최대 중량들을 오름차순 정렬
max_li = []  # 새롭게 비교할 값들을 넣을 리스트

for i in range(n):
    b = li[i] * (n - i)  # 첫번째 값부터 순서대로 전체에서 하나씩 빼가며 곱한다
    max_li.append(b)  # 값들을 max_li 리스트에 넣는다

print(max(max_li))  # 리스트에서 최대값이 정답