k = int(input())
li = []

for i in range(k):
    n = int(input())
    if n == 0:
        li.pop()
    else:
        li.append(n)

print(sum(li))