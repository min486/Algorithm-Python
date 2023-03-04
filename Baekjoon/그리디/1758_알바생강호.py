n = int(input())
li = []

for _ in range(n):
    li.append(int(input()))

li.sort(reverse=True)
result = 0

for i in range(n):
    tip = li[i] - i  # (받은등수-1)은 index(i)와 같다
    if tip > 0:
        result += tip

print(result)