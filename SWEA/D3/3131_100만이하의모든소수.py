n = int(1e6)
li = [1] * (n+1)
li[0], li[1] = 0, 0  # 0과 1은 소수가 아님

# 배수 처리
for i in range(2, n+1):
    if li[i] == 1:
        for j in range(i*2, n+1, i):
            li[j] = 0

for k in range(n+1):
    if li[k] == 1:
        print(k, end=' ')