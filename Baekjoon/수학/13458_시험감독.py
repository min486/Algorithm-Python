N = int(input())
li = list(map(int, input().split()))
B, C = map(int, input().split())

res = N  # 총감독관은 시험장의 개수만큼
for i in li:
    if i-B > 0:  # 총감독관이 감독 후 인원이 남으면
        res += (i-B+C-1) // C
print(res)