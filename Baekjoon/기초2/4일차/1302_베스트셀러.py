N = int(input())
dic = {}

for i in range(N):
    book = input()
    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 1

mx = max(dic.values())
li = []

for k, v in dic.items():
    if v == mx:
        li.append(k)

print(sorted(li)[0])