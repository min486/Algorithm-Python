n, k = map(int,input().split())
li = list(map(int,input().split()))
hap, cnt = 0, 0
result = []

for i in range(len(li)):
    hap += li[i]
    cnt += 1

    if cnt == k:
        cnt -= 1
        result.append(hap)
        hap -= li[i-k+1]

print(max(result))