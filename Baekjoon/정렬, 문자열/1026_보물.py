N = int(input())
a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))

a_li.sort()  # 오름차순
b_li.sort(reverse=True)  # 내림차순

res = 0
for i in range(N):
    res += a_li[i] * b_li[i]

print(res)