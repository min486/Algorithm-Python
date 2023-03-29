n, m = map(int, input().split())
li = list(map(int, input().split()))

i, j, cnt, total = 0, 0, 0, 0

while True:
    if total >= m:
        total -= li[i]
        i += 1
    elif j == n:
        break
    else:
        total += li[j]
        j += 1

    # i부터 j까지의 합이 m이 되는 경우
    if total == m:
        cnt += 1

print(cnt)