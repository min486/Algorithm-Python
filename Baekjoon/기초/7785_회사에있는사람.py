n = int(input())
dic = {}

for _ in range(n):
    name = input().split()
    dic[name[0]] = name[1]

li = []
for k, v in dic.items():
    if v == 'enter':
        li.append(k)

result = reversed(sorted(li))
for i in result:
    print(i)