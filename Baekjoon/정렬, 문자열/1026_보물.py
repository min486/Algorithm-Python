n = int(input())
a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))
result = 0

for i in range(n):
    result += min(a_li) * max(b_li)
    a_li.pop(a_li.index(min(a_li)))
    b_li.pop(b_li.index(max(b_li)))

print(result)