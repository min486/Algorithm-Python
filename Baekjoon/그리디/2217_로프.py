n = int(input())
li = []

for _ in range(n):
    li.append(int(input()))

li.sort()
weight_li = []

# 작은 값부터 확인 (현재 중량 * 남은 중량 개수)
for i in range(n):
    weight = li[i] * (n - i)  
    weight_li.append(weight)

print(max(weight_li))  # 들어올릴 수 있는 최대 중량