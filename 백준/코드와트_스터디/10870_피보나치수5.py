n = int(input())
pibo = [0, 1]

# 앞에 두 수의 합이므로 2번째 인덱스부터 시작
for i in range(2, n+1):
    pibo.append(pibo[i-1] + pibo[i-2])

print(pibo[n])