N, M = map(int, input().split())

# set - in함수의 시간복잡도는 O(1)
# list - in함수의 시간복잡도는 O(n)
a_set = set()
b_set = set()
res = []

for _ in range(N):
    a_set.add(input())
for _ in range(M):
    b_set.add(input())

for i in a_set:
    if i in b_set:
        res.append(i)

res.sort()
print(len(res), *res, sep='\n')