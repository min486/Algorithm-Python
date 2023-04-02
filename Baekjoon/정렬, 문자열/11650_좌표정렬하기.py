n = int(input())
li = []

for _ in range(n):
    x, y = map(int, input().split())
    li.append([x, y])

result = sorted(li, key=lambda x : (x[0], x[1]))

for i in range(len(result)):
    print(*result[i])