arr = [list(map(int, input().split())) for _ in range(5)]

li = []
for _ in range(5):
    li += list(map(int, input().split()))

cnt_li = [0] * 26
for i in range(5):
    for j in range(5):
        cnt_li[arr[i][j]] = (i, j)

visit = [[0] * 10 for _ in range(4)]

for n in li:
    i, j = cnt_li[n]
    visit[0][j] += 1
    visit[1][i] += 1
    visit[2][i-j] += 1
    visit[3][i+j] += 1
    cnt = 0 
    for v in visit:
        cnt += v.count(5)
    if cnt >= 3:
        break

print(sum(v[0]))