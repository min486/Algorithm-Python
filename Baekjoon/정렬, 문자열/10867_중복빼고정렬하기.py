n = int(input())
li = list(map(int, input().split()))

result = sorted(set(li))

print(*result)