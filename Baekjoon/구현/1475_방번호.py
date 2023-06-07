cnt = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}

n = input()

for i in range(len(n)):
    if n[i] in ['6', '9']:
        cnt['6'] += 1
    else :
        cnt[n[i]] += 1

if cnt['6'] % 2 == 0:
    cnt['6'] = cnt['6'] // 2
else:
    cnt['6'] = cnt['6'] // 2 + 1

print(max(cnt.values()))