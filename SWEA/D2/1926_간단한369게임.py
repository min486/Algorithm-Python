N = int(input())

li = ['3', '6', '9']

for i in range(1, N + 1):
    cnt = 0
    for j in str(i):
        if j in li:
            cnt += 1
    if cnt > 0:
        i = '-' * cnt
    
    print(i, end = ' ')