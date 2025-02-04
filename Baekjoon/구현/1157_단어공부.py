word = input().upper()
dic = {}

for i in word:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

li = []
for k, v in dic.items():
    if v == max(dic.values()):
        li.append(k)

if len(li) == 1:
    print(li[0])
else:
    print("?")
