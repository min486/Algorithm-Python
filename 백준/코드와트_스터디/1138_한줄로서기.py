N = int(input())
li = list(map(int,input().split()))
result = [0 for _ in range(N)]
'''
[0,0,1,0] 0을 2개 지난 이후 1 위치
[0,2,1,0] 0을 1개 지난 이후 2 위치
[0,2,1,3] 0을 1개 지난 이후 3 위치
[4,2,1,3] 0을 0개 지난 이후 4 위치
'''
for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == li[i] and result[j] == 0:
            result[j] = i + 1
            break
        elif result[j] == 0:
            cnt += 1

print(*result)