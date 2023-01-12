N = int(input())
dic = {}

for i in range(N):
    file = input().split('.')[1]
    if file in dic:
        dic[file] += 1
    else:
        dic[file] = 1

result = sorted(dic.items())

for k, v in result:
    print(k, v)