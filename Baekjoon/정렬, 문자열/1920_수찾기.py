n = int(input())
n_li = list(map(int, input().split()))
m = int(input())
m_li = list(map(int, input().split()))
dic = {}

for i in n_li:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for j in m_li:
    if j in dic:
        print(1)
    else:
        print(0)