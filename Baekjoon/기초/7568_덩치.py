n = int(input())
li = []

for _ in range(n):
    wei, hei = map(int, input().split())
    li.append([wei, hei])

# 이중반복문을 이용해 키&몸무게 비교
for i in range(n):
    rank = 1
    for j in range(n):
        if (li[i][0] < li[j][0]) and (li[i][1] < li[j][1]):
            rank += 1

    print(rank, end=' ')