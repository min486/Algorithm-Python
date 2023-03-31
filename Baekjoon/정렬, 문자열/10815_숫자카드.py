n = int(input())
n_li = list(map(int, input().split()))
m = int(input())
m_li = list(map(int, input().split()))

# 시간초과 나서 딕셔너리 사용
dic = {}

for i in n_li:
    dic[i] = 0

for j in m_li:
    if j in dic:
        print(1, end=' ')
    else:
        print(0, end=' ')