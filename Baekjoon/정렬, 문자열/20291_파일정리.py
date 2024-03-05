N = int(input())
dic = {}

for _ in range(N):
    back = input().split('.')[1]
    
    if back in dic:
        dic[back] += 1
    else:
        dic[back] = 1

# {'txt': 3, 'spc': 2, 'icpc': 2, 'world': 1}
# -> [('icpc', 2), ('spc', 2), ('txt', 3), ('world', 1)]
res = sorted(dic.items())

for k, v in res:
    print(k, v)