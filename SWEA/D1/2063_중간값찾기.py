N = int(input())
 
li = list(map(int, input().split()))
li.sort()
 
result = N // 2
 
print(li[result])