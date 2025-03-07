n = int(input())
li = list(map(int, input().split()))

li.sort()
div = n // 2

print(li[div])