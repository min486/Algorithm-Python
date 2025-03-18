text = input().upper()
dct = {}

for i in text:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1

li = []
for k, v in dct.items():
    if v == max(dct.values()):
        li.append(k)

if len(li) == 1:
    print(li[0])
else:
    print('?')