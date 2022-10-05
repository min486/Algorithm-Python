n, m = map(int, input().split())
li = list(map(int, input().split()))

i, j, cnt, total = 0, 0, 0, 0

while(True):
    if total >= m:
        total -= li[i]
        i += 1
    elif j == n:
        break
    else:
        total += li[j]
        j += 1

    if total == m:
        cnt += 1

print(cnt)
