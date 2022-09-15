n = int(input())
pibo = [0, 1]

for i in range(2, n+1):
    pibo.append(pibo[i-1] + pibo[i-2])

print(pibo[n])