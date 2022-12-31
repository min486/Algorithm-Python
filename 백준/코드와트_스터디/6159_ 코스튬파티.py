n, s = map(int, input().split())
li = []

for _ in range(n):
    cow = int(input())
    if cow < s:
        li.append(cow)

li.sort(reverse=True)
cnt = 0

for _ in range(len(li)):
    po = li.pop()
    if po > (s // 2):
        break

    for i in li:
        if i <= (s - po):
            cnt += 1

print(cnt)
