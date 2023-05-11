n = int(1e6) + 1
li = [1] * n
li[0], li[1] = 0, 0  # 0과 1은 소수가 아님

# 배수 처리
for i in range(2, n):
    if li[i] == 1:
        for j in range(i*2, n, i):
            li[j] = 0

for k in range(n):
    if li[k] == 1:
        print(k, end=' ')