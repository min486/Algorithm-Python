n = int(input())
dic = {}

for i in range(n):
    file = input().split('.')[1]
    if file in dic:
        dic[file] += 1
    else:
        dic[file] = 1

# dic -> {'txt': 3, 'spc': 2, 'icpc': 2, 'world': 1}
result = sorted(dic.items())  # [('icpc', 2), ('spc', 2), ('txt', 3), ('world', 1)]

for k, v in result:
    print(k, v)